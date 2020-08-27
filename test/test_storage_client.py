from test.fixtures.questions import VALID_QUESTION
import pytest
import boto3
from storage_client import StorageClient

s3_client = boto3.client('s3')
storage_client = StorageClient(s3_client)

def test_storage_client_instantiation():
    assert storage_client.client == s3_client

def test_valid_study_guide_id_returns_question():
    valid_study_guide_id = 'zc7k2nb'

    actual_question = storage_client.select(valid_study_guide_id)

    assert actual_question == VALID_QUESTION

def test_invalid_study_guide_id_raises_exception():
    valid_study_guide_id = 'z123abc'

    with pytest.raises(Exception) as error:
        storage_client.select(valid_study_guide_id)

    assert str(error.value) == f'[NOT FOUND]: No questions found for studyGuideId: {valid_study_guide_id}'

