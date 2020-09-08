import random
import boto3
import numpy as np
from scipy.stats import beta
from storage_client import StorageClient

client = StorageClient(boto3.client('s3'))


def choose_random_question(study_guide_id_list):
    study_guide_id = random.choice(study_guide_id_list)

    return client.select_question_by_study_guide_id(study_guide_id)


def choose_question(study_guide_id_list, confidence_intervals_list):
    study_guide_id = __choose_next_study_guide_id(
        study_guide_id_list, confidence_intervals_list)

    return client.select_question_by_study_guide_id(study_guide_id)


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


def calculate_mastery_and_confidence(
        study_guide_score, study_guide_attempts, topic_score, topic_attempts
):
    average_study_guide_mastery = __calculate_beta_distribution_mean(
        study_guide_score, study_guide_attempts)
    average_topic_mastery = __calculate_beta_distribution_mean(
        topic_score, topic_attempts)

    study_guide_samples = __generate_random_samples(
        study_guide_score, study_guide_attempts)
    topic_samples = __generate_random_samples(topic_score, topic_attempts)

    study_guide_weighting = __calculate_thompson_sampling(
        study_guide_samples, topic_samples)
    if average_study_guide_mastery < average_topic_mastery:
        study_guide_weighting = (1 - study_guide_weighting)

    weighted_score = __calculate_weighted_value(
        study_guide_weighting, study_guide_score, topic_score)

    weighted_attempts = __calculate_weighted_value(
        study_guide_weighting, study_guide_attempts, topic_attempts)

    mastery = __calculate_beta_distribution_mean(
        weighted_score, weighted_attempts)

    weighted_samples = __generate_random_samples(
        weighted_score, weighted_attempts)

    confidence_interval = __calculate_confidence_interval(weighted_samples)

    return mastery, confidence_interval


def __calculate_beta_distribution_mean(score, attempts):
    return (score + 1) / ((score + 1) + (attempts + 1 - score))


def __generate_random_samples(score, attempts):
    return beta.rvs((score + 1), ((attempts - score) + 1), size=1000)


def __calculate_thompson_sampling(sample1, sample2):
    return np.mean(sample1 > sample2)


def __calculate_weighted_value(weighting, study_guide_value, topic_value):
    return weighting * study_guide_value \
        + (1 - weighting) * topic_value


def __calculate_confidence_interval(samples):
    return np.percentile(samples, 95) - np.percentile(samples, 5)
