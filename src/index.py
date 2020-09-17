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
            'nextQuestion': algorithm.choose_next_question(topic_id_for_study_guide_id, study_guide_id_list)
        }

        return __build_response(200, next_question)

    topic_score_and_attempts = __initialise_score_and_attempts(topic_id_list)
    study_guide_score_and_attempts = __initialise_score_and_attempts(
        study_guide_id_list)

    for question in questions:
        __update_topic_score_and_attempts(topic_score_and_attempts, question)
        __update_study_guide_score_and_attempts(
            study_guide_score_and_attempts, question)

    results_list = []
    confidence_intervals_list = []

    for study_guide_id in study_guide_id_list:
        topic_id = topic_id_for_study_guide_id[study_guide_id]
        topic_score = topic_score_and_attempts[topic_id]['score']
        topic_attempts = topic_score_and_attempts[topic_id]['attempts']

        study_guide_score = study_guide_score_and_attempts[study_guide_id]['score']
        study_guide_attempts = study_guide_score_and_attempts[study_guide_id]['attempts']

        weighted_score, weighted_attempts = algorithm.calculate_weighted_score_and_attempts(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)

        mastery, confidence_interval = algorithm.calculate_mastery_and_confidence(
            weighted_score, weighted_attempts)

        confidence_intervals_list.append(confidence_interval)

        mastery_band, band_confidence = algorithm.calculate_mastery_band_and_confidence(
            mastery, weighted_score, weighted_attempts)

        results_list.append({
            'studyGuideId': study_guide_id,
            'topicId': topic_id,
            'band': mastery_band,
            'masteryScore': mastery * 100,
            'confidenceScore': band_confidence * 100
        })

    next_question = {
        'nextQuestion': algorithm.choose_question(study_guide_id_list, confidence_intervals_list)
    }

    if return_results:
        next_question.update({
            'results': results_list
        })

    return __build_response(200, next_question)


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
