from test.fixtures.events import INVALID_EVENT, \
    VALID_EVENT_NO_QUESTIONS, \
    VALID_EVENT_NO_RESULTS, VALID_EVENT_WITH_RESULTS
from test.fixtures.questions import NEXT_QUESTION, \
    VALID_QUESTION_RESPONSE_NO_RESULTS, VALID_QUESTION_RESPONSE_WITH_RESULTS
import pytest
from index import handler

CONTEXT = None


def test_invalid_event_raises_exception():
    with pytest.raises(Exception) as error:
        handler(INVALID_EVENT, CONTEXT)

    assert str(error.value) == '[BAD REQUEST]: Invalid event'


def test_valid_event_initial_question(mocker):
    random_question_mock = mocker.patch(
        'algorithm.choose_initial_question')
    random_question_mock.return_value = NEXT_QUESTION

    actual_question = handler(VALID_EVENT_NO_QUESTIONS, CONTEXT)

    assert actual_question == VALID_QUESTION_RESPONSE_NO_RESULTS


def test_valid_event_with_results_returns_next_question(mocker):

    mastery_and_confidence_mock = mocker.patch(
        'algorithm.calculate_mastery_and_confidence')
    mastery_and_confidence_mock.return_value = 0.75, 0.50

    band_mock = mocker.patch('algorithm.calculate_mastery_band_and_confidence')
    band_mock.return_value = 3, 0.65

    question_mock = mocker.patch('algorithm.choose_next_question')
    question_mock.return_value = NEXT_QUESTION

    actual_question = handler(VALID_EVENT_WITH_RESULTS, CONTEXT)

    assert actual_question == VALID_QUESTION_RESPONSE_WITH_RESULTS


def test_valid_event_no_results_returns_next_question(mocker):

    mastery_and_confidence_mock = mocker.patch(
        'algorithm.calculate_mastery_and_confidence')
    mastery_and_confidence_mock.return_value = 0.75, 0.50

    band_mock = mocker.patch('algorithm.calculate_mastery_band_and_confidence')
    band_mock.return_value = 3, 0.65

    question_mock = mocker.patch('algorithm.choose_next_question')
    question_mock.return_value = NEXT_QUESTION

    actual_question = handler(VALID_EVENT_NO_RESULTS, CONTEXT)

    assert actual_question == VALID_QUESTION_RESPONSE_NO_RESULTS
