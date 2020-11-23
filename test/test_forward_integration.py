import pytest
import algorithm


@pytest.mark.fint_calculate_study_guide_weighting
def test_calculate_study_guide_weighting_passes_into_calculate_weighted_value():
    study_guide_score = 0.
    study_guide_attempts = 100.
    topic_score = 100.
    topic_attempts = 100.

    study_guide_weighting = algorithm.calculate_study_guide_weighting(
        study_guide_score, study_guide_attempts, topic_score, topic_attempts)

    try:
        algorithm.calculate_weighted_value(
            study_guide_weighting, study_guide_score, topic_score)
        assert True
    except:
        assert False