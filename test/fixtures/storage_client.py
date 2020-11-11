VALID_SELECT_RESPONSE = {
    'ResponseMetadata':
    {
        'RequestId': 'A3040AB8A8CEBDBB',
        'HostId': 'EvGJ0a62UFUgMDwwqH1iVbkODeHn7jyxO22ZkxIG6T6py3FQfMFGLWMk4Xb4u9wvOsUsny+f5Lw=',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amz-id-2':
            'EvGJ0a62UFUgMDwwqH1iVbkODeHn7jyxO22ZkxIG6T6py3FQfMFGLWMk4Xb4u9wvOsUsny+f5Lw=',
            'x-amz-request-id': 'A3040AB8A8CEBDBB',
            'date': 'Sun, 06 Sep 2020 18:18:32 GMT',
            'transfer-encoding': 'chunked',
            'server': 'AmazonS3'
        },
        'RetryAttempts': 0
    },
    'Payload': [{
        'Records': {
            'Payload': b'{"id":"eea2b6fd-60ed-45e0-9d82-b216344a8908","text":"Which of these pairs are both gametes?","options":[{"id":"1ea25bba-97b2-459f-a4cb-eeab739c0a0a","text":"Sperm and ovum","response":"A sperm and an ovum are both gametes.  The sperm is the male gamete and the ovum is the female gamete.","isCorrect":true},{"id":"50241537-e049-4219-bb5a-c5e602363206","text":"Ovum and zygote","response":"A sperm and an ovum are both gametes.  A zygote is an ovum which has been fertilised by a sperm.","isCorrect":false},{"id":"143b72e9-e218-46f0-be77-f1fc8a71caeb","text":"Zygote and sperm","response":"A sperm and an ovum are both gametes.  A zygote is an ovum which has been fertilised by a sperm.","isCorrect":false}]},'
        }
    }]
}

VALID_SELECT_PARSED_RESPONSE = [{
    'id': 'eea2b6fd-60ed-45e0-9d82-b216344a8908',
    'text': 'Which of these pairs are both gametes?',
    'options': [
        {
            'id': '1ea25bba-97b2-459f-a4cb-eeab739c0a0a',
            'text': 'Sperm and ovum',
            'response': 'A sperm and an ovum are both gametes.  The sperm is the male gamete and the ovum is the female gamete.',
            'isCorrect': True
        },
        {
            'id': '50241537-e049-4219-bb5a-c5e602363206',
            'text': 'Ovum and zygote', 'response': 'A sperm and an ovum are both gametes.  A zygote is an ovum which has been fertilised by a sperm.',
            'isCorrect': False
        },
        {
            'id': '143b72e9-e218-46f0-be77-f1fc8a71caeb',
            'text': 'Zygote and sperm',
            'response': 'A sperm and an ovum are both gametes.  A zygote is an ovum which has been fertilised by a sperm.',
            'isCorrect': False
        }
    ]
}]

NO_RECORDS_SELECT_RESPONSE = {
    'ResponseMetadata':
    {
        'RequestId': 'A3040AB8A8CEBDBB',
        'HostId': 'EvGJ0a62UFUgMDwwqH1iVbkODeHn7jyxO22ZkxIG6T6py3FQfMFGLWMk4Xb4u9wvOsUsny+f5Lw=',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amz-id-2':
            'EvGJ0a62UFUgMDwwqH1iVbkODeHn7jyxO22ZkxIG6T6py3FQfMFGLWMk4Xb4u9wvOsUsny+f5Lw=',
            'x-amz-request-id': 'A3040AB8A8CEBDBB',
            'date': 'Sun, 06 Sep 2020 18:18:32 GMT',
            'transfer-encoding': 'chunked',
            'server': 'AmazonS3'
        },
        'RetryAttempts': 0
    },
    'Payload': [{}]
}

INVALID_BINARY_SELECT_RESPONSE = {
    'ResponseMetadata':
    {
        'RequestId': 'A3040AB8A8CEBDBB',
        'HostId': 'EvGJ0a62UFUgMDwwqH1iVbkODeHn7jyxO22ZkxIG6T6py3FQfMFGLWMk4Xb4u9wvOsUsny+f5Lw=',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amz-id-2':
            'EvGJ0a62UFUgMDwwqH1iVbkODeHn7jyxO22ZkxIG6T6py3FQfMFGLWMk4Xb4u9wvOsUsny+f5Lw=',
            'x-amz-request-id': 'A3040AB8A8CEBDBB',
            'date': 'Sun, 06 Sep 2020 18:18:32 GMT',
            'transfer-encoding': 'chunked',
            'server': 'AmazonS3'
        },
        'RetryAttempts': 0
    },
    'Payload': [{
        'Records': {
            'Payload': b'invalid JSON binary'
        }
    }]
}
