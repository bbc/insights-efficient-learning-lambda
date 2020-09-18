VALID_QUESTION = {
    "id": "1",
    "text": "What will happen if a spray of perfume is released into one corner of a room?",
    "options": [
        {
            "id": "1",
            "text": "Particles of the perfume will move by osmosis but remain most concentrated in the corner where they were sprayed",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will move by diffusion and not by osmosis",
            "isCorrect": False
        },
        {
            "id": "2",
            "text": "Particles of the perfume will diffuse until they are spread evenly through the room ",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. This happens because of the random movement of particles of the perfume through the air in the room",
            "isCorrect": True
        },
        {
            "id": "3",
            "text": "The movement of the particles of the perfume will be limited so they will remain concentrated in the corner of the room ",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will not remain concentrated in one corner of the room - because of the random movement of particles of the perfume, it becomes spread through the air in the room",
            "isCorrect": False
        }
    ]
}

NEXT_QUESTION = {
    "id": "1",
    "text": "What will happen if a spray of perfume is released into one corner of a room?",
    "studyGuideId": "zc7k2nb",
    "options": [
        {
            "id": "1",
            "text": "Particles of the perfume will move by osmosis but remain most concentrated in the corner where they were sprayed",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will move by diffusion and not by osmosis",
            "isCorrect": False
        },
        {
            "id": "2",
            "text": "Particles of the perfume will diffuse until they are spread evenly through the room ",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. This happens because of the random movement of particles of the perfume through the air in the room",
            "isCorrect": True
        },
        {
            "id": "3",
            "text": "The movement of the particles of the perfume will be limited so they will remain concentrated in the corner of the room ",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will not remain concentrated in one corner of the room - because of the random movement of particles of the perfume, it becomes spread through the air in the room",
            "isCorrect": False
        }
    ]
}

FORMATTED_QUESTION = {
    "id": "1",
    "text": "What will happen if a spray of perfume is released into one corner of a room?",
    "studyGuideId": "zc7k2nb",
    "topicId": "z2s8v9q",
    "options": [
        {
            "id": "1",
            "text": "Particles of the perfume will move by osmosis but remain most concentrated in the corner where they were sprayed",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will move by diffusion and not by osmosis",
            "isCorrect": False
        },
        {
            "id": "2",
            "text": "Particles of the perfume will diffuse until they are spread evenly through the room ",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. This happens because of the random movement of particles of the perfume through the air in the room",
            "isCorrect": True
        },
        {
            "id": "3",
            "text": "The movement of the particles of the perfume will be limited so they will remain concentrated in the corner of the room ",
            "response": "Particles of the perfume will diffuse until they are spread evenly through the room. They will not remain concentrated in one corner of the room - because of the random movement of particles of the perfume, it becomes spread through the air in the room",
            "isCorrect": False
        }
    ]
}

VALID_QUESTION_RESPONSE_NO_RESULTS = {
    'statusCode': 200,
    'body': {
        'nextQuestion': FORMATTED_QUESTION
    }
}

VALID_QUESTION_RESPONSE_WITH_RESULTS = {
    'statusCode': 200,
    'body': {
        'nextQuestion': {
            'id': '1',
            'text': 'What will happen if a spray of perfume is released into one corner of a room?',
            'studyGuideId': 'zc7k2nb',
            'topicId': 'z2s8v9q',
            'options': [
                {
                    'id': '1',
                    'text': 'Particles of the perfume will move by osmosis but remain most concentrated in the corner where they were sprayed',
                    'response': 'Particles of the perfume will diffuse until they are spread evenly through the room. They will move by diffusion and not by osmosis',
                    'isCorrect': False
                },
                {
                    'id': '2',
                    'text': 'Particles of the perfume will diffuse until they are spread evenly through the room ',
                    'response': 'Particles of the perfume will diffuse until they are spread evenly through the room. This happens because of the random movement of particles of the perfume through the air in the room',
                    'isCorrect': True
                },
                {
                    'id': '3',
                    'text': 'The movement of the particles of the perfume will be limited so they will remain concentrated in the corner of the room ',
                    'response': 'Particles of the perfume will diffuse until they are spread evenly through the room. They will not remain concentrated in one corner of the room - because of the random movement of particles of the perfume, it becomes spread through the air in the room',
                    'isCorrect': False
                }
            ]
        },
        'results': [
            {
                'studyGuideId': 'zc7k2nb',
                'topicId': 'z2s8v9q',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'z84jtv4',
                'topicId': 'z2s8v9q',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'zs8y4qt',
                'topicId': 'z2s8v9q',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'zt8t3k7',
                'topicId': 'z9236yc',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'zxr7ng8',
                'topicId': 'z9236yc',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'z3tgw6f',
                'topicId': 'z9236yc',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            },
            {
                'studyGuideId': 'z8fkmsg',
                'topicId': 'z9236yc',
                'band': 3,
                'masteryScore': 75.0,
                'confidenceScore': 65.0
            }
        ]
    }
}

VALID_QUESTION_ID_LIST = [{
    "id": "1"
}]
