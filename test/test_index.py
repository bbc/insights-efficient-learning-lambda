from test.fixtures.events import INVALID_EVENT, \
    VALID_EVENT_NO_QUESTIONS, \
    VALID_EVENT_NO_RESULTS, VALID_EVENT_WITH_RESULTS
from test.fixtures.questions import NEXT_QUESTION, \
    VALID_QUESTION_RESPONSE_NO_RESULTS, VALID_QUESTION_RESPONSE_WITH_RESULTS
from test.fixtures.config import STUDY_GUIDES_IDS_PER_TOPIC_ID, TOPIC_ID_PER_STUDY_GUIDE_ID

import pytest
from index import handler

CONTEXT = None


def test_invalid_event_raises_exception():
    with pytest.raises(Exception) as error:
        handler(INVALID_EVENT, CONTEXT)

    assert str(error.value) == '[BAD REQUEST]: Invalid event'


def test_valid_event_initial_question(mocker):

    get_study_guide_id_list_mock = mocker.patch(
        'helper.get_study_guide_id_list')
    get_study_guide_id_list_mock.return_value = {}

    get_topic_id_mock = mocker.patch(
        'helper.get_topic_id')
    get_topic_id_mock.return_value = {}

    random_question_mock = mocker.patch(
        'algorithm.choose_initial_question')
    random_question_mock.return_value = NEXT_QUESTION

    actual_question = handler(VALID_EVENT_NO_QUESTIONS, CONTEXT)

    assert actual_question == VALID_QUESTION_RESPONSE_NO_RESULTS


def test_valid_event_with_results_returns_next_question(mocker):

    get_study_guide_id_list_mock = mocker.patch(
        'helper.get_study_guide_id_list')
    get_study_guide_id_list_mock.return_value = ['zc7k2nb', 'z84jtv4', 'zs8y4qt', 'zt8t3k7', 'zxr7ng8', 'z3tgw6f', 'z8fkmsg']

    get_topic_id_mock = mocker.patch(
        'helper.get_topic_id')
    get_topic_id_mock.return_value = {'zc7k2nb': 'z2s8v9q', 'z84jtv4': 'z2s8v9q', 'zs8y4qt': 'z2s8v9q', 'zt8t3k7': 'z9236yc', 'zxr7ng8': 'z9236yc', 'z3tgw6f': 'z9236yc', 'z8fkmsg': 'z9236yc'}

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
    get_study_guide_id_list_mock = mocker.patch(
        'helper.get_study_guide_id_list')
    get_study_guide_id_list_mock.return_value = ['zc7k2nb', 'z84jtv4', 'zs8y4qt', 'zt8t3k7', 'zxr7ng8', 'z3tgw6f', 'z8fkmsg']

    get_topic_id_mock = mocker.patch(
        'helper.get_topic_id')
    get_topic_id_mock.return_value = {'zc7k2nb': 'z2s8v9q', 'z84jtv4': 'z2s8v9q', 'zs8y4qt': 'z2s8v9q', 'zt8t3k7': 'z9236yc', 'zxr7ng8': 'z9236yc', 'z3tgw6f': 'z9236yc', 'z8fkmsg': 'z9236yc'}

    mastery_and_confidence_mock = mocker.patch(
        'algorithm.calculate_mastery_and_confidence')
    mastery_and_confidence_mock.return_value = 0.75, 0.50

    band_mock = mocker.patch('algorithm.calculate_mastery_band_and_confidence')
    band_mock.return_value = 3, 0.65

    question_mock = mocker.patch('algorithm.choose_next_question')
    question_mock.return_value = NEXT_QUESTION

    actual_question = handler(VALID_EVENT_NO_RESULTS, CONTEXT)

    assert actual_question == VALID_QUESTION_RESPONSE_NO_RESULTS
