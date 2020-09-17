from test.fixtures.storage_client import VALID_SELECT_RESPONSE, INVALID_BINARY_SELECT_RESPONSE, \
    VALID_SELECT_PARSED_RESPONSE, NO_RECORDS_SELECT_RESPONSE
from test.fixtures.questions import VALID_QUESTION, VALID_QUESTION_ID_LIST
import os
import boto3
import pytest
from botocore.exceptions import ClientError, ParamValidationError
from storage_client import StorageClient

s3 = boto3.client('s3')
storage_client = StorageClient(s3)

VALID_KEY = 'quizzes/questions/z2296yc.json'
VALID_EXPRESSION = "SELECT * FROM S3OBJECT s"

def test_storage_client_instantiation():
    assert storage_client.client == s3


def test_storage_client_returns_event(mocker):
    select_mock = mocker.patch.object(s3, 'select_object_content')
    select_mock.return_value = VALID_SELECT_RESPONSE

    response = storage_client.select(VALID_KEY, VALID_EXPRESSION)

    assert response == VALID_SELECT_PARSED_RESPONSE

def test_storage_client_raises_exceptions_when_invalid_binary(mocker):
    select_mock = mocker.patch.object(s3, 'select_object_content')
    select_mock.return_value = INVALID_BINARY_SELECT_RESPONSE

    with pytest.raises(Exception) as error:
        storage_client.select(VALID_KEY, VALID_EXPRESSION)

    assert str(
        error.value) == '[S3 CLIENT ERROR]: An error occurred, could not parse binary'

def test_storage_client_raises_exceptions_when_invalid_parameter(mocker):
    select_mock = mocker.patch.object(s3, 'select_object_content')
    select_mock.side_effect = ParamValidationError(report='Error Report')

    invalid_key = ''
    invalid_expression = ''

    with pytest.raises(Exception) as error:
        storage_client.select(invalid_key, invalid_expression)

    assert str(
        error.value) == '[S3 CLIENT ERROR]: Parameter validation failed:\nError Report'


def test_storage_client_raises_exception_when_client_error(mocker):
    select_mock = mocker.patch.object(s3, 'select_object_content')

    error = {
        "Error": {
            "Code": "Error Code",
            "Message": "Error Message"
        }
    }

    select_mock.side_effect = ClientError(error, 'SelectObjectContent')

    with pytest.raises(Exception) as error:
        storage_client.select(VALID_KEY, VALID_EXPRESSION)

    assert str(
        error.value) == '[S3 CLIENT ERROR]: An error occurred (Error Code) when calling the SelectObjectContent operation: Error Message'


def test_storage_client_raises_exception_when_no_records_in_event(mocker):
    select_mock = mocker.patch.object(s3, 'select_object_content')
    select_mock.return_value = NO_RECORDS_SELECT_RESPONSE

    with pytest.raises(Exception) as error:
        storage_client.select(VALID_KEY, VALID_EXPRESSION)

    assert str(
        error.value) == f'[S3 CLIENT ERROR]: An error occurred, No Records found in response from S3 with key: {VALID_KEY} and expression: {VALID_EXPRESSION}'


def test_select_question_method(mocker):
    mocker.patch('storage_client.BUCKET', "test_bucket")
    mocker.patch('storage_client.FOLDER', "test_folder")

    select_mock = mocker.patch('storage_client.StorageClient.select')
    select_mock.side_effect = [VALID_QUESTION_ID_LIST, [VALID_QUESTION]]

    storage_client.select_question_by_study_guide_id('z2296yc')
    select_mock.assert_called_with('test_folder/z2296yc.json', "SELECT * FROM S3OBJECT s WHERE s.id='1'")