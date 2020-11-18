import algorithm


def is_float_like(value):
    return type(value) in [int, float]


def calculate_weighted_score_and_attempts(undecorated_function):
    def validate_calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts):

        if not is_float_like(study_guide_score):
            raise TypeError(f"study_guide_score should be an int or float, a {study_guide_score.__class__.__name__} was provided")
        if not is_float_like(study_guide_attempts):
            raise TypeError(f"study_guide_attempts should be an int or float, a {study_guide_attempts.__class__.__name__} was provided")
        if not is_float_like(topic_score):
            raise TypeError(f"topic_score should be an int or float, a {topic_score.__class__.__name__} was provided")
        if not is_float_like(topic_attempts):
            raise TypeError(f"topic_attempts should be an int or float, a {topic_attempts.__class__.__name__} was provided")

        if study_guide_score < 0:
            raise ValueError(f"{study_guide_score} < 0 : study_guide_score should be non-negative")
        if study_guide_attempts < 0:
            raise ValueError(f"{study_guide_attempts} < 0 : study_guide_attempts should be non-negative")
        if topic_score < 0:
            raise ValueError(f"{topic_score} < 0 : topic_score should be non-negative")
        if topic_attempts < 0:
            raise ValueError(f"{topic_attempts} < 0 : topic_attempts should be non-negative")

        if study_guide_score > study_guide_attempts:
            raise ValueError(f"{study_guide_score} > {study_guide_attempts} : study_guide_score should be less than or equal to study_guide_attempts")
        if topic_score > topic_attempts:
            raise ValueError(f"{topic_score} > {topic_attempts} : topic_score should be less than or equal to topic_attempts")
        if study_guide_attempts > topic_attempts:
            raise ValueError(f"{study_guide_attempts} > {topic_attempts} : study_guide_attempts should be less than or equal to topic_attempts")
        if study_guide_score > topic_score:
            raise ValueError(f"{study_guide_score} > {topic_score} : study_guide_score should be less than or equal to topic_score")

        return undecorated_function(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)

    return validate_calculate_weighted_score_and_attempts
