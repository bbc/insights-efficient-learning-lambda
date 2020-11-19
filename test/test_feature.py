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
