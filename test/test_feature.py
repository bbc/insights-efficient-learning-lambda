import pytest
import algorithm


# -----------------------------------------
# Feature tests on calculate_weighted_value
# -----------------------------------------

@pytest.mark.feature_calculate_weighted_value
def test_calculate_weighted_value_returns_float():
    weighted_value = \
        algorithm._calculate_weighted_value(0.5, 1., 2.)
    assert isinstance(weighted_value, float)


@pytest.mark.feature_calculate_weighted_value
def test_calculate_weighted_value_between_study_guide_and_topic_value():
    weighting = 0.5
    study_guide_value = 1.
    topic_value = 2.
    weighted_value = \
        algorithm._calculate_weighted_value(
            weighting, study_guide_value, topic_value)
    assert weighted_value >= study_guide_value
    assert weighted_value <= topic_value


@pytest.mark.feature_calculate_weighted_value
def test_calculate_weighted_value_is_study_guidewhen_weighting_is_1():
    weighting = 1.
    study_guide_value = 1.
    topic_value = 2.
    weighted_value = \
        algorithm._calculate_weighted_value(
            weighting, study_guide_value, topic_value)
    assert weighted_value == study_guide_value


# ----------------------------------------------
# Feature tests on calculate_confidence_interval
# ----------------------------------------------

@pytest.mark.feature_calculate_confidence_interval
def test_calculate_confidence_interval_returns_float():
    confidence = \
        algorithm._calculate_confidence_interval(1., 2.)
    assert isinstance(confidence, float)


@pytest.mark.feature_calculate_confidence_interval
def test_calculate_confidence_interval_in_range_0_to_1():
    confidence = \
        algorithm._calculate_confidence_interval(1., 2.)
    assert confidence == pytest.approx(0.5, abs=0.5)


# -------------------------------------------------------------
# Feature tests on convert_confidence_interval_into_probability
# -------------------------------------------------------------

@pytest.mark.feature_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_returns_list():
    confidence_intervals = [1., 2., 3.]
    list_of_probabilities = \
        algorithm._convert_confidence_interval_into_probability(confidence_intervals)
    assert isinstance(list_of_probabilities, list)


@pytest.mark.feature_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_returns_floats():
    confidence_intervals = [1., 2., 3.]
    list_of_probabilities = \
        algorithm._convert_confidence_interval_into_probability(confidence_intervals)
    assert all([isinstance(probability, float) for probability in list_of_probabilities])


@pytest.mark.feature_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_probabilities_nonnegative():
    confidence_intervals = [1., 2., 3.]
    list_of_probabilities = \
        algorithm._convert_confidence_interval_into_probability(confidence_intervals)
    assert all([probability >= 0 for probability in list_of_probabilities])


@pytest.mark.feature_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_probabilities_sum_to_1():
    confidence_intervals = [1., 2., 3.]
    list_of_probabilities = \
        algorithm._convert_confidence_interval_into_probability(confidence_intervals)
    assert sum(list_of_probabilities) == 1


@pytest.mark.feature_convert_confidence_interval_into_probability
def test_convert_confidence_interval_into_probability_probabilities_monotonic():
    confidence_intervals = [2., 1., 3.]
    list_of_probabilities = \
        algorithm._convert_confidence_interval_into_probability(confidence_intervals)
    assert list_of_probabilities[2] == max(list_of_probabilities)
    assert list_of_probabilities[1] == min(list_of_probabilities)


# -------------------------------------------------------------
# Feature tests on convert_confidence_interval_into_probability
# -------------------------------------------------------------

@pytest.mark.feature_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_returns_float():
    score = 1.
    attempts = 2.
    mastery = algorithm._calculate_beta_distribution_mean(score, attempts)
    assert isinstance(mastery, float)


@pytest.mark.feature_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_in_range_0_to_1():
    score = 1.
    attempts = 2.
    mastery = algorithm._calculate_beta_distribution_mean(score, attempts)
    assert mastery == pytest.approx(0.5, abs=0.5)


@pytest.mark.feature_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_is_half():
    score = 1.
    attempts = 2.
    mastery = algorithm._calculate_beta_distribution_mean(score, attempts)
    assert mastery == 0.5


@pytest.mark.feature_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_is_2_thirds():
    score = 1.
    attempts = 1.
    mastery = algorithm._calculate_beta_distribution_mean(score, attempts)
    assert mastery == 2 / 3


@pytest.mark.feature_calculate_beta_distribution_mean
def test_calculate_beta_distribution_mean_is_1_thirds():
    score = 0.
    attempts = 1.
    mastery = algorithm._calculate_beta_distribution_mean(score, attempts)
    assert mastery == 1 / 3