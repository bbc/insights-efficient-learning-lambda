import algorithm
import helper

# pylint: disable=too-many-locals
# pylint: disable=unused-argument


def handler(event, context):
    try:
        topic_id_list = event['topicIds']
        questions = event['questions']
        return_results = event['returnResults']
    except KeyError:
        raise Exception('[BAD REQUEST]: Invalid event')

    study_guide_id_list = helper.get_study_guide_id_list(
        topic_id_list)

    topic_id_for_study_guide_id = helper.get_topic_id(
        study_guide_id_list)

    if not questions:
        next_question = {
            'nextQuestion': algorithm.choose_initial_question(topic_id_for_study_guide_id, study_guide_id_list)
        }

        return __build_response(200, next_question)

    question_id_list = __get_question_ids_list(questions)

    study_guide_score_and_attempts, topic_score_and_attempts = __get_topic_and_guide_score_and_attempts(
        topic_id_list, study_guide_id_list, questions)

    weighted_score_and_attempts = __calculate_weighted_score_and_attempts(
        study_guide_score_and_attempts, topic_score_and_attempts,
        topic_id_for_study_guide_id)

    if return_results:
        response = {
            'results': []
        }
        for study_guide_id, guide_weighted_score_and_attempts in weighted_score_and_attempts.items():

            weighted_score, weighted_attempts = __get_weighted_score_and_attempts(
                guide_weighted_score_and_attempts)

            mastery = algorithm.calculate_beta_distribution_mean(
                weighted_score, weighted_attempts)

            mastery_band, band_confidence = algorithm.calculate_mastery_band_and_confidence(
                mastery, weighted_score, weighted_attempts)

            response['results'].append({
                'studyGuideId': study_guide_id,
                'topicId': topic_id_for_study_guide_id[study_guide_id],
                'band': mastery_band,
                'masteryScore': mastery * 100,
                'confidenceScore': band_confidence * 100
            })
    else:
        confidence_intervals_list = __calculate_confidence_intervals_list(
            study_guide_id_list, weighted_score_and_attempts)

        response = {
            'nextQuestion': algorithm.choose_next_question(
                topic_id_for_study_guide_id, study_guide_id_list,
                confidence_intervals_list, question_id_list)
        }

    return __build_response(200, response)


def __get_weighted_score_and_attempts(weighted_score_and_attempts):
    return weighted_score_and_attempts['score'], weighted_score_and_attempts['attempts']


def __calculate_weighted_score_and_attempts(
        study_guide_score_and_attempts, topic_score_and_attempts,
        topic_id_for_study_guide_id):

    study_guide_id_list = list(study_guide_score_and_attempts.keys())
    weighted_score_and_attempts = __initialise_score_and_attempts(study_guide_id_list)

    for study_guide_id, guide_weighted_score_and_attempts in weighted_score_and_attempts.items():
        topic_id = topic_id_for_study_guide_id[study_guide_id]
        topic_score = topic_score_and_attempts[topic_id]['score']
        topic_attempts = topic_score_and_attempts[topic_id]['attempts']

        study_guide_score = study_guide_score_and_attempts[study_guide_id]['score']
        study_guide_attempts = study_guide_score_and_attempts[study_guide_id]['attempts']

        study_guide_weighting = algorithm.get_study_guide_weighting(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)

        guide_weighted_score_and_attempts['score'] = algorithm.calculate_weighted_value(
            study_guide_weighting, study_guide_score, topic_score)

        guide_weighted_score_and_attempts['attempts'] = algorithm.calculate_weighted_value(
            study_guide_weighting, study_guide_attempts, topic_attempts)

    return weighted_score_and_attempts


def __calculate_confidence_intervals_list(study_guide_id_list,
                                          weighted_score_and_attempts):
    confidence_intervals_list = []
    for study_guide_id in study_guide_id_list:
        weighted_score = weighted_score_and_attempts[study_guide_id]['score']
        weighted_attempts = weighted_score_and_attempts[study_guide_id]['attempts']

        confidence_intervals_list.append(algorithm.calculate_confidence_interval(
            weighted_score, weighted_attempts))
    return confidence_intervals_list


def __get_question_ids_list(questions):
    return [question['id'] for question in questions]


def __get_topic_and_guide_score_and_attempts(topic_id_list, study_guide_id_list,
                                             questions):

    topic_score_and_attempts = __initialise_score_and_attempts(topic_id_list)
    study_guide_score_and_attempts = __initialise_score_and_attempts(
        study_guide_id_list)

    for question in questions:
        __update_topic_score_and_attempts(topic_score_and_attempts, question)
        __update_study_guide_score_and_attempts(
            study_guide_score_and_attempts, question)

    return study_guide_score_and_attempts, topic_score_and_attempts


def __initialise_score_and_attempts(list_):
    return {
        key: {
            'score': 0,
            'attempts': 0
        } for key in list_
    }


def __update_topic_score_and_attempts(topic_score_and_attempts, question):
    topic_id = question['topicId']
    score = question['isCorrect']

    topic_score_and_attempts[topic_id]['score'] += score
    topic_score_and_attempts[topic_id]['attempts'] += 1


def __update_study_guide_score_and_attempts(study_guide_score_and_attempts, question):
    study_guide_id = question['studyGuideId']
    score = question['isCorrect']

    study_guide_score_and_attempts[study_guide_id]['score'] += score
    study_guide_score_and_attempts[study_guide_id]['attempts'] += 1


def __build_response(code, body):
    return {
        'statusCode': code,
        'body': body
    }
