def _add_docstring(function, docstring):
    function.__doc__ = docstring
    return function


def calculate_weighted_score_and_attempts(function):
    docstring = """
Compares the results for a study guide against the results aggregated across all studyguides within the topic

Parameters
----------
study_guide_score : non-negative int or float
    score for the study guide
study_guide_attempts : non-negative int or float
    number of questions attempted for the study guide
topic_score : non-negative int or float
    score for the topic
topic_attempts : non-negative int or float
    number of questions attempted from all study guides in the topic

Returns
-------
Weighting between study guide score and attempts and the corresponding topic score and attempts. 
    float in range [0, 1]
    1.0 : When study_guide_score << topic_score
    1.0 : When study_guide_score >> topic_score 

Raises
------
TypeError : study_guide_score should be an int or float, a {study_guide_score.__class__.__name__} was provided
    when study_guide_score is anything except an int or float
TypeError : study_guide_attempts should be an int or float, a {study_guide_attempts.__class__.__name__} was provided
    when study_guide_attempts is anything except an int or float
TypeError : topic_score should be an int or float, a {topic_score.__class__.__name__} was provided
    when topic_score is anything except an int or float
TypeError : topic_attempts should be an int or float, a {topic_attempts.__class__.__name__} was provided
    when topic_attempts is anything except an int or float

ValueError : {study_guide_score} < 0 : study_guide_score should be non-negative
    when study_guide_score is negative
ValueError : {study_guide_attempts} < 0 : study_guide_attempts should be non-negative
    when study_guide_score is negative
ValueError : {topic_score} < 0 : topic_score should be non-negative
    when topic_score is negative
ValueError : {topic_attempts} < 0 : topic_attempts should be non-negative
    when topic_attempts is negative

ValueError : {study_guide_score} > {study_guide_attempts} : study_guide_score should be less than or equal to study_guide_attempts
    when study_guide_score is > study_guide_attempts
ValueError : {topic_score} > {topic_attempts} : topic_score should be less than or equal to topic_attempts
    when topic_score is > topic_attempts
ValueError : {study_guide_attempts} > {topic_attempts} : study_guide_attempts should be less than or equal to topic_attempts
    when study_guide_attempts > topic_attempts
"""
    return _add_docstring(function, docstring)
