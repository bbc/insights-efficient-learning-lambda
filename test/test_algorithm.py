from test.fixtures.questions import VALID_QUESTION, VALID_QUESTION_ID_LIST
import pytest
import algorithm


def test_choose_random_question_returns_question(mocker):
    select_mock = mocker.patch('storage_client.StorageClient.select')
    select_mock.side_effect = [VALID_QUESTION_ID_LIST, [VALID_QUESTION]]

    study_guide_list = ['zc7k2nb']

    actual_question = algorithm.choose_random_question(study_guide_list)

    assert actual_question == VALID_QUESTION


def test_choose_question_returns_question(mocker):
    select_mock = mocker.patch('storage_client.StorageClient.select')
    select_mock.side_effect = [VALID_QUESTION_ID_LIST, [VALID_QUESTION]]

    study_guide_list = ['zc7k2nb', 'zs8y4qt']
    confidence_intervals_list = [0.70, 0]

    actual_question = algorithm.choose_question(
        study_guide_list, confidence_intervals_list)

    assert actual_question == VALID_QUESTION


def test_calculate_mastery_and_confidence_interval():
    actual_mastery, actual_confidence = algorithm.calculate_mastery_and_confidence(
        1, 1, 1, 1)

    assert actual_confidence == pytest.approx(0.75, abs=0.05)
    assert actual_mastery == pytest.approx(0.6666666, abs=0.01)
