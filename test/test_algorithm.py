from test.fixtures.questions import VALID_QUESTION
import pytest
import algorithm


def test_choose_random_question_returns_question():
    study_guide_list = ['zc7k2nb']

    actual_question = algorithm.choose_random_question(study_guide_list)

    assert actual_question == VALID_QUESTION


def test_choose_question_returns_question():
    study_guide_list = ['zc7k2nb', 'zs8y4qt']
    confidence_intervals_list = [0.70, 0]

    actual_question = algorithm.choose_question(
        study_guide_list, confidence_intervals_list)

    assert actual_question == VALID_QUESTION


def test_calculate_mastery_and_confidence_interval():
    actual_mastery, actual_confidence = algorithm.calculate_mastery_and_confidence(
        1, 1, 1, 1)

    assert actual_confidence == pytest.approx(0.70, 0.80)
    assert actual_mastery == pytest.approx(0.6666666)
