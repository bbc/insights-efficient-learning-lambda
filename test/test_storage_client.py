from test.fixtures.storage_client import VALID_SELECT_RESPONSE, INVALID_BINARY_SELECT_RESPONSE, \
    VALID_SELECT_PARSED_RESPONSE, NO_RECORDS_SELECT_RESPONSE
from test.fixtures.questions import VALID_QUESTION, VALID_SINGLE_QUESTION_ID_LIST
from test.fixtures.config import STUDY_GUIDES_IDS_PER_TOPIC_ID, TOPIC_ID_PER_STUDY_GUIDE_ID

import io
import json
from unittest.mock import patch
import pytest
import boto3

from botocore.exceptions import ClientError, ParamValidationError
from storage_client import StorageClient

s3 = boto3.client('s3')
storage_client = StorageClient(s3)

BUCKET = 'bucket'
STUDY_GUIDE_ID = 'z1a2b3c'
KEY = 'folder/z1a2b3c.json'
EXPRESSION_TYPE = 'SQL'
EXPRESSION = 'expression'
INPUT_SERIALIZATION = {"JSON": {"Type": "Document"}}
OUTPUT_SERIALIZATION = {"JSON": {"RecordDelimiter": ","}}
FOLDER = 'folder'
CONFIG_FOLDER = 'config'


@pytest.fixture(autouse=True)
def mock_environment(mocker):
    mocker.patch('storage_client.BUCKET', BUCKET)
    mocker.patch('storage_client.FOLDER', FOLDER)
    mocker.patch('storage_client.CONFIG_FOLDER', CONFIG_FOLDER)


def test_storage_client_instantiation():
    assert storage_client.client == s3


@patch.object(s3, 'select_object_content')
def test_select_returns_response_with_record(mock):

    mock.return_value = VALID_SELECT_RESPONSE

    response = storage_client.select(STUDY_GUIDE_ID, EXPRESSION)

    assert response == VALID_SELECT_PARSED_RESPONSE

    mock.assert_called_with(Bucket=BUCKET, Key=KEY, ExpressionType=EXPRESSION_TYPE, Expression=EXPRESSION,
                            InputSerialization=INPUT_SERIALIZATION, OutputSerialization=OUTPUT_SERIALIZATION)


@patch.object(s3, 'select_object_content')
def test_select_return_empty_array_with_no_records(mock):

    mock.return_value = NO_RECORDS_SELECT_RESPONSE

    response = storage_client.select(STUDY_GUIDE_ID, EXPRESSION)

    assert response == []

    mock.assert_called_with(Bucket=BUCKET, Key=KEY, ExpressionType=EXPRESSION_TYPE, Expression=EXPRESSION,
                            InputSerialization=INPUT_SERIALIZATION, OutputSerialization=OUTPUT_SERIALIZATION)


@patch.object(s3, 'select_object_content')
def test_select_propegates_client_exception(mock):

    client_error = {
        "Error": {
            "Code": "code_value",
            "Message": "message_value"
        }
    }

    mock.side_effect = ClientError(client_error, 'operation_name')

    expected_error_message = '[S3 CLIENT ERROR]: An error occurred (code_value) when calling the operation_name operation: message_value'

    try:
        storage_client.select(STUDY_GUIDE_ID, EXPRESSION)
    except Exception as error:
        assert str(error) == expected_error_message


@patch.object(s3, 'select_object_content')
def test_select_propegates_param_validation_exception(mock):

    mock.side_effect = ParamValidationError(report='error report')

    expected_error_message = '[S3 CLIENT ERROR]: Parameter validation failed:\nerror report'

    try:
        storage_client.select(STUDY_GUIDE_ID, EXPRESSION)
    except Exception as error:
        assert str(error) == expected_error_message


@patch.object(s3, 'select_object_content')
def test_select_throws_exception_when_unable_to_parse_response(mock):

    mock.return_value = INVALID_BINARY_SELECT_RESPONSE

    expected_error_message = '[S3 CLIENT ERROR]: Expecting value: line 1 column 2 (char 1)'

    try:
        storage_client.select(STUDY_GUIDE_ID, EXPRESSION)
    except Exception as error:
        assert str(error) == expected_error_message


def test_select_throws_excpetion_when_missing_study_guide_id():

    expected_error_message = '[S3 CLIENT ERROR]: Missing required parameter: study_guide_id'

    try:
        storage_client.select(None, EXPRESSION)
    except Exception as error:
        assert str(error) == expected_error_message


def test_select_throws_excpetion_when_missing_expression():

    expected_error_message = '[S3 CLIENT ERROR]: Missing required parameter: expression'

    try:
        storage_client.select(STUDY_GUIDE_ID, None)
    except Exception as error:
        assert str(error) == expected_error_message


@patch.object(storage_client, 'select')
def test_select_all_question_ids_returns_question_ids(mock):

    expected_expression = "SELECT s.id FROM S3OBJECT s"

    mock.return_value = VALID_SINGLE_QUESTION_ID_LIST

    question_ids = storage_client.select_all_question_ids(STUDY_GUIDE_ID)

    assert question_ids == VALID_SINGLE_QUESTION_ID_LIST

    mock.assert_called_with(STUDY_GUIDE_ID, expected_expression)


@patch.object(storage_client, 'select')
def test_select_and_filter_question_ids_returns_question_ids(mock):

    question_id_list = ['2']
    expected_expression = "SELECT s.id FROM S3OBJECT s WHERE NOT s.id IN ['2']"

    mock.return_value = VALID_SINGLE_QUESTION_ID_LIST

    question_id_list = storage_client.select_and_filter_question_ids(
        STUDY_GUIDE_ID, question_id_list)

    assert question_id_list == VALID_SINGLE_QUESTION_ID_LIST

    mock.assert_called_with(STUDY_GUIDE_ID, expected_expression)


def test_select_and_filter_question_ids_throws_exception_when_missing_question_id_list():

    expected_error_message = '[S3 CLIENT ERROR]: Missing required parameter: question_id_list'

    try:
        storage_client.select_and_filter_question_ids(STUDY_GUIDE_ID, None)
    except Exception as error:
        assert str(error) == expected_error_message


@patch.object(storage_client, 'select')
def test_select_question_by_id_returns_question(mock):
    question_id = '1'
    expected_expression = "SELECT * FROM S3OBJECT s WHERE s.id='1'"

    mock.return_value = [VALID_QUESTION]

    question = storage_client.select_question_by_id(
        question_id, STUDY_GUIDE_ID)

    assert question == VALID_QUESTION

    mock.assert_called_with(STUDY_GUIDE_ID, expected_expression)


@patch.object(storage_client, 'select')
def test_select_question_by_id_returns_none_when_no_question(mock):
    question_id = '1'
    expected_expression = "SELECT * FROM S3OBJECT s WHERE s.id='1'"

    mock.return_value = []

    question = storage_client.select_question_by_id(
        question_id, STUDY_GUIDE_ID)

    assert question is None

    mock.assert_called_with(STUDY_GUIDE_ID, expected_expression)


@patch.object(storage_client, 'get_file')
def test_get_study_guide_ids_per_topic_ids(mock):

    expected_file_name = 'config/STUDY_GUIDES_IDS_PER_TOPIC_ID.json'

    mock.return_value = STUDY_GUIDES_IDS_PER_TOPIC_ID

    results = storage_client.get_study_guide_ids_per_topic_ids()

    mock.assert_called_with(expected_file_name)
    assert results == STUDY_GUIDES_IDS_PER_TOPIC_ID


@patch.object(storage_client, 'get_file')
def test_get_topic_id_per_study_guide_id(mock):

    expected_file_name = 'config/TOPIC_ID_PER_STUDY_GUIDE_ID.json'

    mock.return_value = TOPIC_ID_PER_STUDY_GUIDE_ID

    results = storage_client.get_topic_id_per_study_guide_id()

    mock.assert_called_with(expected_file_name)
    assert results == TOPIC_ID_PER_STUDY_GUIDE_ID


@patch.object(s3, 'get_object')
def test_get_file_returns_data(mock):

    json_body = io.BytesIO(json.dumps('json_body').encode())

    mock.side_effect = [{"Body": json_body}]

    file_name = 'valid_filename'

    assert storage_client.get_file(file_name) == 'json_body'


@patch.object(s3, 'get_object')
def test_get_file_raises_exceptions_with_invalid_key(mock):

    client_error = {
        "Error": {
            "Code": "code_value",
            "Message": "message_value"
        }
    }

    mock.side_effect = ClientError(client_error, 'operation_name')

    invalid_key = 'invalid_filename'

    try:
        storage_client.get_file(invalid_key)
    except Exception as error:
        assert str(
            error) == "[S3 CLIENT ERROR]: An error occurred (code_value) when calling the operation_name operation: message_value"
