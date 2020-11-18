import pytest
import algorithm


# -------------------------------------------------------------------
# Validation tests on algorithm.calculate_weighted_score_and_attempts
# -------------------------------------------------------------------

@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_typeerror_on_study_guide_score():
    study_guide_score = '1'
    study_guide_attempts = 1.
    topic_score = 1.
    topic_attempts = 1.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"study_guide_score should be an int or float, a {study_guide_score.__class__.__name__} was provided"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_typeerror_on_study_guide_attempts():
    study_guide_score = 1
    study_guide_attempts = '1.'
    topic_score = 1.
    topic_attempts = 1.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"study_guide_attempts should be an int or float, a {study_guide_attempts.__class__.__name__} was provided"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_typeerror_on_topic_score():
    study_guide_score = 1
    study_guide_attempts = 1
    topic_score = '1.'
    topic_attempts = 1.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"topic_score should be an int or float, a {topic_score.__class__.__name__} was provided"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_typeerror_on_topic_attempts():
    study_guide_score = 1
    study_guide_attempts = 1
    topic_score = 1.
    topic_attempts = '1.'
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"topic_attempts should be an int or float, a {topic_attempts.__class__.__name__} was provided"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_study_guide_score_nonnegative():
    study_guide_score = -1
    study_guide_attempts = 1.
    topic_score = 1.
    topic_attempts = 1.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_score} < 0 : study_guide_score should be non-negative"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_study_guide_attempts_nonnegative():
    study_guide_score = 1
    study_guide_attempts = -1.
    topic_score = 1.
    topic_attempts = 1.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_attempts} < 0 : study_guide_attempts should be non-negative"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_topic_score_nonnegative():
    study_guide_score = 1
    study_guide_attempts = 1.
    topic_score = -1.
    topic_attempts = 1.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{topic_score} < 0 : topic_score should be non-negative"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_topic_attempts_nonnegative():
    study_guide_score = 1
    study_guide_attempts = 1.
    topic_score = 1.
    topic_attempts = -1.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{topic_attempts} < 0 : topic_attempts should be non-negative"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_study_guide_score_lt_attempts():
    study_guide_score = 2
    study_guide_attempts = 1.
    topic_score = 1.
    topic_attempts = 1.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_score} > {study_guide_attempts} : study_guide_score should be less than or equal to study_guide_attempts"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_topic_score_lt_attempts():
    study_guide_score = 1
    study_guide_attempts = 1.
    topic_score = 2.
    topic_attempts = 1.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{topic_score} > {topic_attempts} : topic_score should be less than or equal to topic_attempts"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_study_guide_attempts_lt_topic_attempts():
    study_guide_score = 1
    study_guide_attempts = 3.
    topic_score = 1.
    topic_attempts = 1.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_attempts} > {topic_attempts} : study_guide_attempts should be less than or equal to topic_attempts"


@pytest.mark.validation_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_study_guide_score_lt_topic_score():
    study_guide_score = 2
    study_guide_attempts = 3.
    topic_score = 1.
    topic_attempts = 3.
    try:
        algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts,
            topic_score, topic_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{study_guide_score} > {topic_score} : study_guide_score should be less than or equal to topic_score"


# ------------------------------------------------------------
# Validation tests on algorithm._calculate_confidence_interval
# ------------------------------------------------------------

@pytest.mark.validation_calculate_confidence_interval
def test_calculate_confidence_interval_weighted_score_is_float():
    weighted_score = '2'
    weighted_attempts = 3.
    try:
        algorithm._calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"weighted_score should be a float, a {weighted_score.__class__.__name__} was provided"


@pytest.mark.validation_calculate_confidence_interval
def test_calculate_confidence_interval_weighted_attempts_is_float():
    weighted_score = 2.
    weighted_attempts = '3'
    try:
        algorithm._calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"weighted_attempts should be a float, a {weighted_attempts.__class__.__name__} was provided"


@pytest.mark.validation_calculate_confidence_interval
def test_calculate_confidence_interval_weighted_score_is_nonnegative():
    weighted_score = -2.
    weighted_attempts = 3.
    try:
        algorithm._calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{weighted_score} < 0 : weighted_score should be non-negative"


@pytest.mark.validation_calculate_confidence_interval
def test_calculate_confidence_interval_weighted_attempts_is_nonnegative():
    weighted_score = 2.
    weighted_attempts = -3.
    try:
        algorithm._calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{weighted_attempts} < 0 : weighted_attempts should be non-negative"


@pytest.mark.validation_calculate_confidence_interval
def test_calculate_confidence_interval_weighted_score_lt_attempts():
    weighted_score = 5.
    weighted_attempts = 3.
    try:
        algorithm._calculate_confidence_interval(
            weighted_score, weighted_attempts)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"{weighted_score} > {weighted_attempts} : weighted_score should be less than or equal to weighted_attempts"
