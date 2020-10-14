import random
import boto3
import numpy as np
from scipy.optimize import fsolve
from scipy.stats import beta
from storage_client import StorageClient

client = StorageClient(boto3.client('s3'))
BAND1_THRESHOLD = 0.34
BAND3_THRESHOLD = 0.66
CONFIDENCE_THRESHOLD = 0.6


def choose_initial_question(topic_id_for_study_guide_id, study_guide_id_list):
    study_guide_id = random.choice(study_guide_id_list)

    question_id_list = client.select_all_question_ids(study_guide_id)

    question_id = random.choice(question_id_list)['id']

    question = client.select_question_by_id(question_id, study_guide_id)

    question.update({
        "studyGuideId": study_guide_id,
        "topicId": topic_id_for_study_guide_id[study_guide_id]
    })

    return question


def choose_next_question(topic_id_for_study_guide_id, study_guide_id_list, confidence_intervals_list, question_id_list):
    study_guide_id = __choose_next_study_guide_id(
        study_guide_id_list, confidence_intervals_list)

    filtered_question_id_list = client.select_and_filter_question_ids(
        study_guide_id, question_id_list)

    if not filtered_question_id_list:
        index = study_guide_id_list.index(study_guide_id)

        filtered_study_guide_id_list = list(filter(
            lambda x: x != study_guide_id, study_guide_id_list))

        filtered_confidence_intervals_list = list(filter(
            lambda x: confidence_intervals_list.index(x) != index, confidence_intervals_list))

        return choose_next_question(topic_id_for_study_guide_id, filtered_study_guide_id_list, filtered_confidence_intervals_list, question_id_list)

    question_id = random.choice(filtered_question_id_list)['id']

    question = client.select_question_by_id(question_id, study_guide_id)

    question.update({
        "studyGuideId": study_guide_id,
        "topicId": topic_id_for_study_guide_id[study_guide_id]
    })

    return question


def __choose_next_study_guide_id(study_guide_id_list, confidence_intervals_list):
    probabilities_list = __convert_confidence_interval_into_probability(
        confidence_intervals_list)

    return np.random.choice(a=study_guide_id_list, p=probabilities_list)


def __convert_confidence_interval_into_probability(confidence_intervals):
    probabilities_list = [confidence_interval **
                          8 for confidence_interval in confidence_intervals]

    return __normalise_list(probabilities_list)


def __normalise_list(list_):
    return [element / sum(list_) for element in list_]


def calculate_weighted_score_and_attempts(
        study_guide_score, study_guide_attempts, topic_score, topic_attempts):
    average_study_guide_mastery = __calculate_beta_distribution_mean(
        study_guide_score, study_guide_attempts)
    average_topic_mastery = __calculate_beta_distribution_mean(
        topic_score, topic_attempts)

    study_guide_weighting = __calculate_thompson_sampling(
        study_guide_score, study_guide_attempts,
        topic_score, topic_attempts)

    if average_study_guide_mastery < average_topic_mastery:
        study_guide_weighting = (1 - study_guide_weighting)

    weighted_score = __calculate_weighted_value(
        study_guide_weighting, study_guide_score, topic_score)

    weighted_attempts = __calculate_weighted_value(
        study_guide_weighting, study_guide_attempts, topic_attempts)

    return weighted_score, weighted_attempts


def calculate_mastery_and_confidence(
        weighted_score, weighted_attempts
):
    mastery = __calculate_beta_distribution_mean(
        weighted_score, weighted_attempts)

    confidence_interval = __calculate_confidence_interval(
        weighted_score, weighted_attempts)

    return mastery, confidence_interval


def __calculate_beta_distribution_mean(score, attempts):
    return (score + 1) / ((score + 1) + (attempts + 1 - score))


def __thompson_sampling_integrand(mastery, study_guide_score, study_guide_attempts,
                         topic_score, topic_attempts):

    topic_ability_equals_mastery = beta.pdf(
        mastery, 1 + topic_score, 1 + topic_attempts - topic_score)

    study_guide_ability_exceeds_mastery = \
        1 - __calculate_cumulative_probability(
            mastery, study_guide_score, study_guide_attempts)

    return study_guide_ability_exceeds_mastery * topic_ability_equals_mastery


def __calculate_thompson_sampling(study_guide_score, study_guide_attempts,
                                  topic_score, topic_attempts):

    trapezium_edge_points = np.linspace(0, 1, 100)
    trapezium_heights = __thompson_sampling_integrand(
        trapezium_edge_points, study_guide_score, study_guide_attempts,
        topic_score, topic_attempts)

    return np.trapz(y=trapezium_heights, x=trapezium_edge_points)


def __calculate_weighted_value(weighting, study_guide_value, topic_value):
    return weighting * study_guide_value \
        + (1 - weighting) * topic_value


def __5th_percentile_equation(mastery, score, attempts):
    return beta.cdf(mastery, 1 + score, 1 + attempts - score) - 0.05


def __calculate_5th_percentile(score, attempts):
    return fsolve(__5th_percentile_equation, x0=0,
                  args=(score, attempts), xtol=0.1)


def __calculate_95th_percentile(score, attempts):
    return fsolve(__95th_percentile_equation, x0=1,
                  args=(score, attempts), xtol=0.1)


def __95th_percentile_equation(mastery, score, attempts):
    return beta.cdf(mastery, 1 + score, 1 + attempts - score) - 0.95


def __calculate_confidence_interval(score, attempts):
    _95th_percentile = __calculate_95th_percentile(score, attempts)
    _5th_percentile = __calculate_5th_percentile(score, attempts)
    return _95th_percentile - _5th_percentile


def __calculate_cumulative_probability(mastery_threshold, score, attempts):
    return beta.cdf(mastery_threshold, (score + 1), ((attempts - score) + 1))


def __calculate_band1_confidence(score, attempts):
    return __calculate_cumulative_probability(BAND1_THRESHOLD, score, attempts)


def __calculate_band3_confidence(score, attempts):
    return 1 - __calculate_cumulative_probability(BAND3_THRESHOLD, score, attempts)


def __calculate_band2_confidence(score, attempts):
    band_1_confidence = __calculate_cumulative_probability(
        BAND1_THRESHOLD, score, attempts)
    band_1_or_2_confidence = __calculate_cumulative_probability(
        BAND3_THRESHOLD, score, attempts)
    return band_1_or_2_confidence - band_1_confidence


def __calculate_band_confidence(mastery_score, score, attempts):
    band = __place_mastery_in_band(mastery_score)
    if band == 1:
        return __calculate_band1_confidence(score, attempts)
    elif band == 3:
        return __calculate_band3_confidence(score, attempts)
    else:
        return __calculate_band2_confidence(score, attempts)


def __place_mastery_in_band(mastery_score):
    if mastery_score < BAND1_THRESHOLD:
        return 1
    elif mastery_score > BAND3_THRESHOLD:
        return 3
    else:
        return 2


def __calculate_confident_mastery_band(mastery_score, confidence):
    if confidence > CONFIDENCE_THRESHOLD:
        return __place_mastery_in_band(mastery_score)
    else:
        return 2


def calculate_mastery_band_and_confidence(mastery_score, score, attempts):
    confidence = __calculate_band_confidence(mastery_score, score, attempts)
    mastery_band = __calculate_confident_mastery_band(
        mastery_score, confidence)
    return mastery_band, confidence
