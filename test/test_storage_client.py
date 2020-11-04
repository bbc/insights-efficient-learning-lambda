from test.fixtures.storage_client import VALID_SELECT_RESPONSE, INVALID_BINARY_SELECT_RESPONSE, \
    VALID_SELECT_PARSED_RESPONSE, NO_RECORDS_SELECT_RESPONSE
from test.fixtures.questions import VALID_QUESTION, VALID_SINGLE_QUESTION_ID_LIST
from test.fixtures.config import STUDY_GUIDES_IDS_PER_TOPIC_ID, TOPIC_ID_PER_STUDY_GUIDE_ID

import boto3
import pytest
import io
import json
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


def test_select_all_question_ids(mocker):
    mocker.patch('storage_client.BUCKET', "test_bucket")
    mocker.patch('storage_client.FOLDER', "test_folder")

    select_mock = mocker.patch.object(storage_client, 'select')
    select_mock.return_value = VALID_SINGLE_QUESTION_ID_LIST

    study_guide_id = 'zc7k2nb'

    actual_question_id_list = storage_client.select_all_question_ids(
        study_guide_id)

    select_mock.assert_called_with(
        'test_folder/zc7k2nb.json', "SELECT s.id FROM S3OBJECT s")
    assert actual_question_id_list == VALID_SINGLE_QUESTION_ID_LIST


def test_select_and_filter_question_ids(mocker):
    mocker.patch('storage_client.BUCKET', "test_bucket")
    mocker.patch('storage_client.FOLDER', "test_folder")

    select_mock = mocker.patch.object(storage_client, 'select')
    select_mock.return_value = VALID_SINGLE_QUESTION_ID_LIST

    study_guide_id = 'zc7k2nb'
    question_id_list = ['2']

    actual_question_id_list = storage_client.select_and_filter_question_ids(
        study_guide_id, question_id_list)

    select_mock.assert_called_with(
        'test_folder/zc7k2nb.json', "SELECT s.id FROM S3OBJECT s WHERE NOT s.id IN ['2']")
    assert actual_question_id_list == VALID_SINGLE_QUESTION_ID_LIST


def test_select_question_by_id(mocker):
    mocker.patch('storage_client.BUCKET', "test_bucket")
    mocker.patch('storage_client.FOLDER', "test_folder")

    select_mock = mocker.patch.object(storage_client, 'select')
    select_mock.return_value = [VALID_QUESTION]

    question_id = "1"
    study_guide_id = 'zc7k2nb'

    actual_question = storage_client.select_question_by_id(
        question_id, study_guide_id)

    select_mock.assert_called_with(
        'test_folder/zc7k2nb.json', "SELECT * FROM S3OBJECT s WHERE s.id='1'")
    assert actual_question == VALID_QUESTION


def test_get_study_guide_ids_per_topic_ids(mocker):
    mocker.patch('storage_client.BUCKET', "test_bucket")
    mocker.patch('storage_client.CONFIG_FOLDER', "test_config")

    select_mock = mocker.patch.object(storage_client, 'get_file')
    select_mock.return_value = STUDY_GUIDES_IDS_PER_TOPIC_ID

    results = storage_client.get_study_guide_ids_per_topic_ids()

    select_mock.assert_called_with(
        'test_config/STUDY_GUIDES_IDS_PER_TOPIC_ID.json')
    assert results == STUDY_GUIDES_IDS_PER_TOPIC_ID


def test_get_topic_id_per_study_guide_id(mocker):
    mocker.patch('storage_client.BUCKET', "test_bucket")
    mocker.patch('storage_client.CONFIG_FOLDER', "test_config")

    select_mock = mocker.patch.object(storage_client, 'get_file')
    select_mock.return_value = TOPIC_ID_PER_STUDY_GUIDE_ID

    results = storage_client.get_topic_id_per_study_guide_id()

    select_mock.assert_called_with(
        'test_config/TOPIC_ID_PER_STUDY_GUIDE_ID.json')
    assert results == TOPIC_ID_PER_STUDY_GUIDE_ID


def test_get_file_returns_data(mocker):
    json_body = io.BytesIO(json.dumps('json_body').encode())

    select_mock = mocker.patch.object(storage_client.client, 'get_object')
    select_mock.side_effect = [{"Body": json_body}]

    valid_key = 'valid_filename'

    assert storage_client.get_file(valid_key) == 'json_body'


def test_get_file_raises_exceptions_with_invalid_key(mocker):

    invalid_key_error = 'An error occurred (InvalidAccessKeyId) when calling the GetObject operation: The AWS Access Key Id you provided does not exist in our records.'

    get_object_mock = mocker.patch.object(s3, 'get_object')
    get_object_mock.side_effect = Exception(invalid_key_error)

    invalid_key = 'invalid_filename'

    with pytest.raises(Exception) as error:
        storage_client.get_file(invalid_key)

    assert str(
        error.value) == f"[S3 CLIENT ERROR]: {invalid_key_error}"
