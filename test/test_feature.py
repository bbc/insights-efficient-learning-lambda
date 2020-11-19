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


# @pytest.mark.feature_calculate_weighted_score_and_attempts
# def test_calculate_weighted_score_and_attempts_in_range_0_to_1():
#     weighted_score, weighted_attempts = \
#         algorithm.calculate_weighted_score_and_attempts(0., 2., 3., 4.)
#     assert 0.5 == pytest.approx(weighted_score, abs=0.5)
#     assert 0.5 == pytest.approx(weighted_attempts, abs=0.5)
