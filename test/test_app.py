import pytest
from src.app import handler

# pylint: disable=redefined-outer-name
@pytest.fixture
def event():
    return {"message": "This is an Event!"}

@pytest.fixture
def context():
    return {"message": "This is an Context!"}

def test_lambda_handler(event, context):
    actual = handler(event, context)
    assert actual == event
