import json
import pytest
from src.s3_client import S3Client

BUCKET = 'bucket'
KEY = 'key'

# pylint: disable=unused-argument

def test_get_object_returns_valid_object(mock_s3_client):
    body = {"key": "value"}

    mock_s3_client.put_object(Bucket=BUCKET, Key=KEY, Body=json.dumps(body))

    s3_client = S3Client(mock_s3_client)
    retrieved_object = s3_client.get_object(BUCKET, KEY)

    assert retrieved_object == body

def test_get_object_throws_parsing_error(mock_s3_client):
    body = b"key : value"

    mock_s3_client.put_object(Bucket=BUCKET, Key=KEY, Body=body)

    with pytest.raises(Exception, match=('S3 Client Error when parsing JSON')):
        s3_client = S3Client(mock_s3_client)
        s3_client.get_object(BUCKET, KEY)

def test_get_object_throws_client_error(mock_s3_client):
    invalid_key = 'invalid_key'
    with pytest.raises(Exception,
                       match=(f'S3 Client Error when fetching with Key: {invalid_key} from Bucket: {BUCKET}')):
        s3_client = S3Client(mock_s3_client)
        s3_client.get_object(BUCKET, invalid_key)
