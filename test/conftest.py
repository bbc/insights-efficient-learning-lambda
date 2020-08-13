import os
import pytest
import boto3
from moto import mock_s3

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument

@pytest.fixture(scope='module', autouse=True)
def aws_credentials():
    os.environ['AWS_ACCESS_KEY_ID'] = ''
    os.environ['AWS_SECRET_ACCESS_KEY'] = ''
    os.environ['AWS_SESSION_TOKEN'] = ''
    os.environ['AWS_SHARED_CREDENTIALS_FILE'] = ''
    os.environ['AWS_CONFIG_FILE'] = ''

@pytest.fixture(scope='module')
def mock_s3_client(aws_credentials):
    with mock_s3():
        mock_client = boto3.client('s3', region_name='eu-west-1')
        mock_client.create_bucket(Bucket='bucket')
        yield mock_client
