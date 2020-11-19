import pytest
import algorithm


# --------------------------------------------
# Feature tests on weighted_score_and_attempts
# --------------------------------------------

@pytest.mark.feature_calculate_weighted_score_and_attempts
def test_calculate_weighted_score_and_attempts_returns_floats():
    weighted_score, weighted_attempts = \
        algorithm.calculate_weighted_score_and_attempts(0., 2., 3., 4.)
    assert isinstance(weighted_score, float)
    assert isinstance(weighted_attempts, float)