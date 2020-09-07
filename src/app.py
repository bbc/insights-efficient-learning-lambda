import algorithm
import helper


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
            'nextQuestion': algorithm.choose_random_question(study_guide_id_list)
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

        mastery, confidence_interval = algorithm.calculate_mastery_and_confidence(
            study_guide_score, study_guide_attempts, topic_score, topic_attempts)

        confidence_intervals_list.append(confidence_interval)

        results_list.append({
            'studyGuideId': study_guide_id,
            'topicId': topic_id,
            'band': 1,
            'masteryScore': mastery * 100,
            'confidenceScore': (1 - confidence_interval) * 100
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
