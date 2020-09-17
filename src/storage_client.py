import os
import json
import random
from botocore.exceptions import ClientError, ParamValidationError

BUCKET = os.getenv('S3_BUCKET') or ''
FOLDER = os.getenv('S3_FOLDER') or ''

# pylint: disable=too-few-public-methods
class StorageClient:
    def __init__(self, client):
        self.client = client


    def select_question_by_study_guide_id(self, study_guide_id):
        key = f'{FOLDER}/{study_guide_id}.json'

        question_id_list = self.select(key, "SELECT s.id FROM S3OBJECT s")

        question_id = random.choice(question_id_list)['id']

        return self.select(key, f"SELECT * FROM S3OBJECT s WHERE s.id='{question_id}'")[0]

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


def _convert_binary_to_json(binary):
    # remove trailing comma, add array brackets and convert to string
    binary_string = f"[{binary.decode('UTF-8').rstrip(',')}]"

    try:
        return json.loads(binary_string)
    except ValueError:
        raise Exception(
            '[S3 CLIENT ERROR]: An error occurred, could not parse binary')
