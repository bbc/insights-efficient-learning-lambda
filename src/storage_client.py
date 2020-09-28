import os
import json
import random
from botocore.exceptions import ClientError, ParamValidationError

BUCKET = os.getenv('S3_BUCKET') or ''
FOLDER = os.getenv('S3_FOLDER') or ''
CONFIG_FOLDER = os.getenv('S3_CONFIG') or ''

# pylint: disable=too-few-public-methods
# pylint: disable=line-too-long
SELECT_QUESTION_ID_LIST_EXPRESSION = "SELECT s.id FROM S3OBJECT s"
SELECT_FILTERED_QUESTION_ID_LIST_EXPRESSION = "SELECT s.id FROM S3OBJECT s WHERE NOT s.id IN {question_id_list}"
SELECT_QUESTION_BY_ID_EXPRESSION = "SELECT * FROM S3OBJECT s WHERE s.id='{question_id}'"


class StorageClient:
    def __init__(self, client):
        self.client = client

    def select_all_question_ids(self, study_guide_id):
        key = f'{FOLDER}/{study_guide_id}.json'

        return self.select(key, SELECT_QUESTION_ID_LIST_EXPRESSION)

    def select_and_filter_question_ids(self, study_guide_id, question_id_list):
        key = f'{FOLDER}/{study_guide_id}.json'

        return self.select(
            key,
            SELECT_FILTERED_QUESTION_ID_LIST_EXPRESSION.format(
                question_id_list=question_id_list
            )
        )

    def select_question_by_id(self, question_id, study_guide_id):
        key = f'{FOLDER}/{study_guide_id}.json'

        return self.select(
            key,
            SELECT_QUESTION_BY_ID_EXPRESSION.format(question_id=question_id)
        )[0]

    def select(self, key, expression):

        try:
            response = self.client.select_object_content(
                Bucket=BUCKET,
                Key=key,
                ExpressionType='SQL',
                Expression=expression,
                InputSerialization={
                    "JSON": {"Type": "Document"}},
                OutputSerialization={"JSON": {"RecordDelimiter": ","}}
            )

        except (ClientError, ParamValidationError) as error:
            raise Exception(f'[S3 CLIENT ERROR]: {error}')

        for event in response['Payload']:
            if 'Records' in event:
                return _convert_binary_to_json(event['Records']['Payload'])

            # pylint: disable=line-too-long
            raise Exception(
                f'[S3 CLIENT ERROR]: An error occurred, No Records found in response from S3 with key: {key} and expression: {expression}')

    def get_file(self, file_name):    
        response = self.client.get_object(
            Bucket=BUCKET,
            Key=file_name
        )
        
        data = json.loads(response["Body"].read().decode())

        return data

    def get_study_guide_ids_per_topic_ids(self):
        study_guide_ids_per_topic_ids = self.get_file(f'{CONFIG_FOLDER}/STUDY_GUIDES_IDS_PER_TOPIC_ID.json')
        return study_guide_ids_per_topic_ids

    def get_topic_id_per_study_guide_id(self):
        topic_id_per_study_guide_id = self.get_file(f'{CONFIG_FOLDER}/TOPIC_ID_PER_STUDY_GUIDE_ID.json')
        return topic_id_per_study_guide_id

def _convert_binary_to_json(binary):
    # remove trailing comma, add array brackets and convert to string
    binary_string = f"[{binary.decode('UTF-8').rstrip(',')}]"

    try:
        return json.loads(binary_string)
    except ValueError:
        raise Exception(
            '[S3 CLIENT ERROR]: An error occurred, could not parse binary')
