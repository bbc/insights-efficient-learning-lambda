import json
import botocore


class S3Client:
    def __init__(self, client):
        self.client = client

    def get_object(self, bucket, key):
        try:
            retrieved_object = self.client.get_object(Bucket=bucket, Key=key)['Body'].read()
        except botocore.exceptions.ClientError:
            raise Exception(f'S3 Client Error when fetching with Key: {key} from Bucket: {bucket}')

        try:
            return json.loads(retrieved_object)
        except ValueError:
            raise Exception('S3 Client Error when parsing JSON')
