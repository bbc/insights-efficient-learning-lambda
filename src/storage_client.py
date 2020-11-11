import os
import json
from botocore.exceptions import ClientError, ParamValidationError

BUCKET = os.getenv('S3_BUCKET') or ''
FOLDER = os.getenv('S3_FOLDER') or ''
CONFIG_FOLDER = os.getenv('S3_CONFIG') or ''

# pylint: disable=line-too-long
SELECT_QUESTION_ID_LIST_EXPRESSION = "SELECT s.id FROM S3OBJECT s"
SELECT_FILTERED_QUESTION_ID_LIST_EXPRESSION = "SELECT s.id FROM S3OBJECT s WHERE NOT s.id IN {question_id_list}"
SELECT_QUESTION_BY_ID_EXPRESSION = "SELECT * FROM S3OBJECT s WHERE s.id='{question_id}'"


class StorageClient:
    def __init__(self, client):
        self.client = client

    def select(self, study_guide_id, expression):

        if not study_guide_id:
            raise Exception(
                '[S3 CLIENT ERROR]: Missing required parameter: study_guide_id')

        if not expression:
            raise Exception(
                '[S3 CLIENT ERROR]: Missing required parameter: expression')

        key = f'{FOLDER}/{study_guide_id}.json'

        try:
            response = self.client.select_object_content(
                Bucket=BUCKET,
                Key=key,
                ExpressionType='SQL',
                Expression=expression,
                InputSerialization={"JSON": {"Type": "Document"}},
                OutputSerialization={"JSON": {"RecordDelimiter": ","}}
            )

            for event in response['Payload']:

                if not 'Records' in event:
                    return []

                decoded_payload = event['Records']['Payload'].decode('UTF-8')
                stripped_payload = decoded_payload.rstrip(',')
                parsed_response = json.loads(f"[{stripped_payload}]")

                return parsed_response

        except (ClientError, ParamValidationError, ValueError) as error:
            raise Exception(f'[S3 CLIENT ERROR]: {error}')

    def select_all_question_ids(self, study_guide_id):
        return self.select(study_guide_id, SELECT_QUESTION_ID_LIST_EXPRESSION)

    def select_and_filter_question_ids(self, study_guide_id, question_id_list):

        if not question_id_list:
            raise Exception(
                '[S3 CLIENT ERROR]: Missing required parameter: question_id_list')

        return self.select(
            study_guide_id,
            SELECT_FILTERED_QUESTION_ID_LIST_EXPRESSION.format(
                question_id_list=question_id_list
            )
        )

    def select_question_by_id(self, question_id, study_guide_id):

        question_list = self.select(
            study_guide_id,
            SELECT_QUESTION_BY_ID_EXPRESSION.format(question_id=question_id)
        )

        if not question_list:
            return None

        return question_list[0]

    def get_file(self, file_name):
        try:
            response = self.client.get_object(
                Bucket=BUCKET,
                Key=file_name
            )

            decoded_body = response["Body"].read().decode('UTF-8')
            parsed_response = json.loads(decoded_body)

            return parsed_response

        except Exception as error:
            raise Exception(f'[S3 CLIENT ERROR]: {error}')

    def get_study_guide_ids_per_topic_ids(self):
        study_guide_ids_per_topic_ids = self.get_file(
            f'{CONFIG_FOLDER}/STUDY_GUIDES_IDS_PER_TOPIC_ID.json')
        return study_guide_ids_per_topic_ids

    def get_topic_id_per_study_guide_id(self):
        topic_id_per_study_guide_id = self.get_file(
            f'{CONFIG_FOLDER}/TOPIC_ID_PER_STUDY_GUIDE_ID.json')
        return topic_id_per_study_guide_id
