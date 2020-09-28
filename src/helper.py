import itertools
import boto3
from storage_client import StorageClient

client = StorageClient(boto3.client('s3'))

def get_study_guide_id_list(topic_ids):
    dictionary = {}

    study_guide_ids_per_topic_id = client.get_study_guide_ids_per_topic_ids()

    for topic_id in topic_ids:
        try:
            dictionary[topic_id] = study_guide_ids_per_topic_id[topic_id]
        except KeyError:
            raise Exception(
                f'[NOT FOUND]: No studyGuideIds found for topicId: {topic_id}')

    return list(itertools.chain(*dictionary.values()))


def get_topic_id(study_guide_ids):
    dictionary = {}

    topic_id_per_study_guide_id = client.get_topic_id_per_study_guide_id()
    for study_guide_id in study_guide_ids:
        try:
            dictionary[study_guide_id] = topic_id_per_study_guide_id[study_guide_id]
        except KeyError:
            raise Exception(
                f'[NOT FOUND]: No topicId found for studyGuideId: {study_guide_id}')

    return dictionary
