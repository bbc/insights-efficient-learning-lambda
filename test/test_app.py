import pytest
from src.app import handler

class TestAppHandler:
    @pytest.fixture
    def event(self):
        return {"message": "This is an Event!"}
    @pytest.fixture
    def context(self):
        return {"message": "This is an Context!"}

    def test_lambda_handler(self, event, context):
        actual = handler(event, context)
        assert actual == event
