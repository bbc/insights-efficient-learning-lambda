import pytest
import helper

from test.fixtures.config import STUDY_GUIDES_IDS_PER_TOPIC_ID, TOPIC_ID_PER_STUDY_GUIDE_ID


def test_valid_topic_id_list_returns_study_guide_id_list(mocker):

    study_guide_ids_per_topic_id_mock = mocker.patch(
        'storage_client.StorageClient.get_study_guide_ids_per_topic_ids')
    study_guide_ids_per_topic_id_mock.return_value = STUDY_GUIDES_IDS_PER_TOPIC_ID

    valid_topic_id_list = ['z2s8v9q']
    expected_study_guide_id_list = ["zc7k2nb", "z84jtv4", "zs8y4qt"]

    actual_list = helper.get_study_guide_id_list(valid_topic_id_list)

    assert actual_list == expected_study_guide_id_list


def test_multiple_valid_topic_id_list_returns_study_guide_id_list(mocker):

    study_guide_ids_per_topic_id_mock = mocker.patch(
        'storage_client.StorageClient.get_study_guide_ids_per_topic_ids')
    study_guide_ids_per_topic_id_mock.return_value = STUDY_GUIDES_IDS_PER_TOPIC_ID

    valid_topic_id_list = ['z2s8v9q', 'z9236yc']
    expected_study_guide_id_list = [
        'zc7k2nb', 'z84jtv4', 'zs8y4qt', 'zt8t3k7', 'zxr7ng8', 'z3tgw6f', 'z8fkmsg']

    actual_list = helper.get_study_guide_id_list(valid_topic_id_list)

    assert actual_list == expected_study_guide_id_list


def test_invalid_topic_id_raises_exception(mocker):

    study_guide_ids_per_topic_id_mock = mocker.patch(
        'storage_client.StorageClient.get_study_guide_ids_per_topic_ids')
    study_guide_ids_per_topic_id_mock.return_value = STUDY_GUIDES_IDS_PER_TOPIC_ID

    invalid_topic_id = 'z123abc'

    with pytest.raises(Exception) as error:
        helper.get_study_guide_id_list([invalid_topic_id])

    assert str(
        error.value) == f'[NOT FOUND]: No studyGuideIds found for topicId: {invalid_topic_id}'


def test_valid_study_guide_id_list_returns_topic_id_dict(mocker):

    topic_id_per_study_guide_id_mock = mocker.patch(
        'storage_client.StorageClient.get_topic_id_per_study_guide_id')
    topic_id_per_study_guide_id_mock.return_value = TOPIC_ID_PER_STUDY_GUIDE_ID

    valid_study_guide_id_list = ['zc7k2nb']
    expected_topic_id_dict = {'zc7k2nb': 'z2s8v9q'}

    actual_dict = helper.get_topic_id(valid_study_guide_id_list)

    assert actual_dict == expected_topic_id_dict


def test_invalid_study_guide_id_raises_exception(mocker):

    topic_id_per_study_guide_id_mock = mocker.patch(
        'storage_client.StorageClient.get_topic_id_per_study_guide_id')
    topic_id_per_study_guide_id_mock.return_value = TOPIC_ID_PER_STUDY_GUIDE_ID
    invalid_study_guide_id = 'z123abc'

    with pytest.raises(Exception) as error:
        helper.get_topic_id([invalid_study_guide_id])

    assert str(
        error.value) == f'[NOT FOUND]: No topicId found for studyGuideId: {invalid_study_guide_id}'
