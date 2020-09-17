from test.fixtures.questions import NEXT_QUESTION, VALID_QUESTION, VALID_QUESTION_ID_LIST
import pytest
import algorithm


def test_choose_random_study_guide_id():
    study_guide_list = ['zc7k2nb']
    actual_study_guide_id = algorithm.test_choose_random_study_guide_id(
        study_guide_list)
    assert actual_study_guide_id == 'zc7k2nb'


def test_choose_random_question_by_study_guide_id(mocker):
    select_mock = mocker.patch('storage_client.StorageClient.select')
    select_mock.side_effect = [VALID_QUESTION_ID_LIST, [VALID_QUESTION]]

    study_guide_id = 'zc7k2nb'
    actual_question = algorithm.choose_random_question(study_guide_id)
    assert actual_question == VALID_QUESTION


def test_next_question(mocker):
    select_mock = mocker.patch('storage_client.StorageClient.select')
    select_mock.side_effect = [VALID_QUESTION_ID_LIST, [VALID_QUESTION]]

    topic_id_for_study_guide_id = [{'zc7k2nb': 'z2s8v9q'}]
    study_guide_id_list = ['zc7k2nb']

    actual_next_question = algorithm.choose_next_question(
        topic_id_for_study_guide_id, study_guide_id_list)

    assert actual_next_question == NEXT_QUESTION


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
        1, 1)

    assert actual_confidence == pytest.approx(0.75, abs=0.05)
    assert actual_mastery == pytest.approx(0.66, abs=0.01)


def test_get_mastery_band_and_confidence_confident_band1():
    actual_mastery_band, actual_confidence = algorithm.calculate_mastery_band_and_confidence(
        1 / 6, 0, 4)

    assert actual_mastery_band == 1
    assert actual_confidence == pytest.approx(0.87, abs=0.01)


def test_get_mastery_band_and_confidence_uncertain_band2():
    actual_mastery_band, actual_confidence = algorithm.calculate_mastery_band_and_confidence(
        2 / 3, 1, 1)

    assert actual_mastery_band == 2
    assert actual_confidence == pytest.approx(0.56, abs=0.01)


def test_get_mastery_band_and_confidence_confident_band2():
    actual_mastery_band, actual_confidence = algorithm.calculate_mastery_band_and_confidence(
        0.5, 4, 8)

    assert actual_mastery_band == 2
    assert actual_confidence == pytest.approx(0.69, abs=0.01)


def test_get_mastery_band_and_confidence_confident_band3():
    actual_mastery_band, actual_confidence = algorithm.calculate_mastery_band_and_confidence(
        5 / 6, 4, 4)

    assert actual_mastery_band == 3
    assert actual_confidence == pytest.approx(0.87, abs=0.01)
