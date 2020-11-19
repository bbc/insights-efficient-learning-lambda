def _add_docstring(function, docstring):
    function.__doc__ = docstring
    return function


def _calculate_weighted_value(function):
    docstring = """
Takes a weighted average of a value associated with a study guide and the corresponding value for the topic and returns a weighted average. 

Parameters
----------
weighting : float in [0, 1]
    weighting between the study guide results and the topic results
study_guide_value : non-negative int or float
    score or attempts for the study guide
topic_value : non-negative int or float
    score or attempts for the topic

Returns
-------
Weighted average of study_guide_value and topic_value
    float in range [study_guide_value, topic_value]
    study_guide_score : When weighting == 1.0

Raises
------
TypeError : weighting should be a float, a {weighting.__class__.__name__} was provided
    when weighting is anything except a float
TypeError : study_guide_value should be a float, a {study_guide_value.__class__.__name__} was provided
    when study_guide_value is anything except a float
TypeError : topic_value should be a float, a {topic_value.__class__.__name__} was provided
    when topic_value is anything except a float

ValueError : unexpected value encountered - weighted_score should be in the interval [0, 1]
    when weighting is anything outside the interval [0, 1]
ValueError : {study_guide_value} < 0 : study_guide_value should be non-negative
    when study_guide_value is negative
ValueError : {topic_value} < 0 : topic_value should be non-negative
    when topic_value is negative

ValueError : {study_guide_value} > {topic_value} : study_guide_value should be less than or equal to topic_value
    when study_guide_value > topic_value
"""
    return _add_docstring(function, docstring)


def _calculate_confidence_interval(function):
    docstring = """
Calculates the width of the confidence interval given by the 5th and 9th percentile ofthe weighted mastery.

Parameters
----------
weighted_score : non-negative int or float
    weighted score for the study guide
weighted_attempts : non-negative int or float
    weighted number of questions attempted for the study guide

Returns
-------
Confidence interval for the distribution given by the 5th and 9th percentile of the weighted mastery.
    float in range [0, 1]

Raises
------
TypeError : weighted_score should be a float, a {weighted_score.__class__.__name__} was provided
    when weighted_score is anything except float
TypeError : weighted_attempts should be a float, a {weighted_attempts.__class__.__name__} was provided
    when weighted_attempts is anything except a float

ValueError : {weighted_score} < 0 : weighted_score should be non-negative
    when weighted_score is negative
ValueError : {weighted_attempts} < 0 : weighted_attempts should be non-negative
    when weighted_attempts is negative

ValueError : {weighted_score} > {weighted_attempts} : weighted_score should be less than or equal to weighted_attempts
    when weighted_score is > weighted_attempts
"""
    return _add_docstring(function, docstring)


def _convert_confidence_interval_into_probability(function):
    docstring = """
Converts the confidence intervals into probabilities.

Parameters
----------
confidence_intervals_list : list of non-negative floats
    confidence intervals associated with each of the study guides

Returns
-------
list of probabilities associated with each of the study guides. These should be in the same order as the corresponding confidence intervals. 
    list
    list of floats
    all float values should positive
    sum of all values should be 1
    larger probabilities should correspond to larger confidence intervals

Raises
------
TypeError : confidence_intervals_list should be a list, a {confidence_intervals_list.__class__.__name__} was provided
    when confidence_intervals is not a list
TypeError : unexpected type encountered in confidence_intervals_list : expected float, got {confidence_interval.__class__.__name__}
    when non-float value exists in confidence_intervals

ValueError : {confidence_interval} < 0 : all confidence intervals should be non-negative
    when negative value encountered in confidence_intervals_list
"""
    return _add_docstring(function, docstring)


def _calculate_beta_distribution_mean(function):
    docstring = """
Calculates expected value or mean of a beta distribution Beta(alpha, beta), where
alpha = 1 + score
beta = 1 + (attempts - score)
Uses the analytic expression of the form alpha / (alpha + beta).

Parameters
----------
score : non-negative int or float
    score
attempts : non-negative int or float
    number of attempts

Returns
-------
Calculates expected value or mean of a beta distribution.
    float in range [0, 1]
    0.5 when score = 1, attempts = 2
    2/3 when score = 1, attempts = 1
    1/3 when score = 0, attempts = 1

Raises
------
TypeError : score should be an float, a {score.__class__.__name__} was provided
    when score is anything except a float
TypeError : attempts should be a float, a {score.__class__.__name__} was provided
    when attempts is anything except a float

ValueError : {score} < 0 : score should be non-negative
    when score is negative
ValueError : {attempts} < 0 : attempts should be non-negative
    when attempts is negative

ValueError : {score} > {attempts} : score should be less than or equal to attempts
    when score is > attempts
"""
    return _add_docstring(function, docstring)


def _place_mastery_in_band(function):
    docstring = """
Places mastery in either band 1, 2, or 3 based on predetermined thresholds.

Parameters
----------
mastery_score : float in [0, 1]
    Expected value of the mastery for a study guide

Returns
-------
Band 1, 2, or 3.
    one of [1, 2, 3]
    1 when mastery_score = 0
    3 when mastery_score = 1

Raises
------
TypeError : mastery_score should be a float, a {mastery_score.__class__.__name__} was provided
    when mastery_score is anything except a float

ValueError : unexpected value encountered: mastery_score should be in the interval [0, 1]
    when mastery_score is anything outside the interval [0, 1]
"""
    return _add_docstring(function, docstring)


def _calculate_band_confidence(function):
    docstring = """
Calculates the confidence (probability) that  a user's mastery lies within the same band as the expected value of the mastery. Theresholds for the bands are defined externally.

Parameters
----------
mastery_score : float in [0, 1]
    Expected value of the mastery for a study guide
score : non-negative float
    score for a study guide
attempts : non-negative float
    number of questions attempted from a study guide

Returns
-------
Confidence or probability that a user's true mastery lies within the same band as mastery_score
    float in [0, 1]

Raises
------
TypeError : mastery_score should be a float, a {mastery_score.__class__.__name__} was provided
    when mastery_score is anything except a float
TypeError : score should be a float, a {score.__class__.__name__} was provided
    when score is anything except a float
TypeError : attempts should be a float, a {attempts.__class__.__name__} was provided
    when attempts is anything except a float

ValueError : unexpected value encountered : mastery_score should be in the interval [0, 1]
    when mastery_score is anything outside the interval [0, 1]
ValueError : {score} < 0 : score should be non-negative
    when score is negative
ValueError : {attempts} < 0 : attempts should be non-negative
    when attempts is negative

ValueError : {score} > {attempts} : score should be less than or equal to attempts
    when score is > attempts
"""
    return _add_docstring(function, docstring)


def _calculate_confident_mastery_band(function):
    docstring = """
Assigns final banding to a study guide. If we're not confident that a study guide is in band 1 or 3 then default to 2.

Parameters
----------
mastery_score : float in [0, 1]
    Expected value of the mastery for a study guide
confidence : float in [0, 1]
    Confidence that the user's true mastery lies in the same band as mastery_score

Returns
-------
Final banding of a study guide
    one of [1, 2, 3]
    1 if mastery_score = 0 and confidence = 1
    3 if mastery_score = 1 and confidence = 1
    2 if mastery_score = 0 and confidence = 0
    2 if mastery_score = 1 and confidence = 0

Raises
------
TypeError : mastery_score should be a float, a {mastery_score.__class__.__name__} was provided
    when mastery_score is anything except a float
TypeError : confidence should be a float, a {confidence.__class__.__name__} was provided
    when confidence is anything except a float

ValueError : unexpected value encountered - mastery_score should be in the interval [0, 1]
    when mastery_score is anything outside the interval [0, 1]
ValueError : unexpected value encountered - confidence should be in the interval [0, 1]
    when confidence is anything outside the interval [0, 1]
"""
    return _add_docstring(function, docstring)