from test.fixtures.events import INVALID_EVENT, VALID_EVENT_NO_QUESTIONS, \
    VALID_EVENT_NO_RESULTS, VALID_EVENT_WITH_RESULTS
from test.fixtures.questions import VALID_QUESTION, \
    VALID_QUESTION_RESPONSE_NO_RESULTS, VALID_QUESTION_RESPONSE_WITH_RESULTS
import pytest
from index import handler

CONTEXT = None


def test_invalid_event_raises_exception():
    with pytest.raises(Exception) as error:
        handler(INVALID_EVENT, CONTEXT)

    assert str(error.value) == '[BAD REQUEST]: Invalid event'


def test_valid_event_no_questions_returns_random_question(mocker):
    random_question_mock = mocker.patch('algorithm.choose_random_question')
    random_question_mock.return_value = VALID_QUESTION
    expected_study_guide_list = [
        'zc7k2nb', 'z84jtv4', 'zs8y4qt', 'zt8t3k7', 'zxr7ng8', 'z3tgw6f', 'z8fkmsg']

    actual_question = handler(VALID_EVENT_NO_QUESTIONS, CONTEXT)

    random_question_mock.assert_called_with(expected_study_guide_list)
    assert actual_question == VALID_QUESTION_RESPONSE_NO_RESULTS


def test_valid_event_no_results_returns_next_question(mocker):
    question_mock = mocker.patch('algorithm.choose_question')
    question_mock.return_value = VALID_QUESTION

    actual_question = handler(VALID_EVENT_NO_RESULTS, CONTEXT)

    question_mock.assert_called()
    assert actual_question == VALID_QUESTION_RESPONSE_NO_RESULTS


def test_valid_event_with_results_returns_next_question(mocker):
    question_mock = mocker.patch('algorithm.calculate_mastery_and_confidence')
    question_mock.return_value = 0.75, 0.50

    question_mock = mocker.patch('algorithm.choose_question')
    question_mock.return_value = VALID_QUESTION

    actual_question = handler(VALID_EVENT_WITH_RESULTS, CONTEXT)

    assert actual_question == VALID_QUESTION_RESPONSE_WITH_RESULTS
