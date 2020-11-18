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


# ---------------------------------------------------------------------------
# Validation tests on algorithm._convert_confidence_interval_into_probability
# ---------------------------------------------------------------------------

@pytest.mark.validation_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_receives_list():
    confidence_intervals_list = {1, 1, 3}
    try:
        algorithm._convert_confidence_interval_into_probability(
            confidence_intervals_list)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"confidence_intervals_list should be a list, a {confidence_intervals_list.__class__.__name__} was provided"


@pytest.mark.validation_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_contains_floats():
    confidence_intervals_list = [1., '1', 3]
    try:
        algorithm._convert_confidence_interval_into_probability(
            confidence_intervals_list)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"unexpected type encountered in confidence_intervals_list : expected float, got {'1'.__class__.__name__}"


@pytest.mark.validation_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_contains_floats():
    confidence_intervals_list = [1., -1, 3]
    try:
        algorithm._convert_confidence_interval_into_probability(
            confidence_intervals_list)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'ValueError'
        assert str(error) == f"-1 < 0 : all confidence intervals should be non-negative"


# ---------------------------------------------------------------------------
# Validation tests on algorithm._convert_confidence_interval_into_probability
# ---------------------------------------------------------------------------

@pytest.mark.validation_place_mastery_in_band
def test_place_mastery_in_band_receives_float():
    mastery_score = '4'
    try:
        algorithm._place_mastery_in_band(mastery_score)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        assert str(error) == f"mastery_score should be a float, a {mastery_score.__class__.__name__} was provided"


@pytest.mark.validation_place_mastery_in_band
def test_place_mastery_in_band_mastery_in_0_to_1():
    mastery_score = 4
    try:
        algorithm._place_mastery_in_band(mastery_score)
        assert False
    except Exception as error:
        assert error.__class__.__name__ == 'TypeError'
        # assert str(error) == f"mastery_score should be a float, a {mastery_score.__class__.__name__} was provided"
