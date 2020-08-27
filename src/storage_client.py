import random

class StorageClient:
    def __init__(self, client):
        self.client = client

    def select(self, study_guide_id):
        try:
            return random.choice(QUESTIONS[study_guide_id])
        except KeyError:
            raise Exception(f'[NOT FOUND]: No questions found for studyGuideId: {study_guide_id}')

QUESTIONS = {
                "zc7k2nb" : [{
                                "id": "1",
                                "text": "What will happen if a spray of perfume is released into one corner of a room?",
                                "options": [{
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
                                }]
                            }],

                "zs8y4qt" : [{
                                "id": "2",
                                "text": "Which statement is true of genes?",
                                "options": [{
                                    "id": "1",
                                    "text": "A gene is a short section of DNA that codes for a protein",
                                    "response": "A gene is a short section of DNA that codes for a protein. It is estimated that there are around 20 000 to 25 000 genes that code for proteins.",
                                    "isCorrect": True
                                },
                                {
                                    "id": "2",
                                    "text": "A single molecule of DNA",
                                    "response": "A gene is a short section of DNA that codes for a protein. A chromosome, not in its dividing state, is made from a single molecule of DNA",
                                    "isCorrect": False
                                },
                                {
                                    "id": "3",
                                    "text": "Humans have 46 genes",
                                    "response": "A gene is a short section of DNA that codes for a protein. Humans have 46 chromosomes.",
                                    "isCorrect": False
                                }]
                            }],

                "zt8t3k7" : [{
                                "id": "4",
                                "text": "What part of pathogens do antibodies bind to?",
                                "options": [{
                                    "id": "1",
                                    "text": "Antigens",
                                    "response": "Antibodies bind to antigens on pathogens.",
                                    "isCorrect": True
                                },
                                {
                                    "id": "2",
                                    "text": "Antitoxins",
                                    "response": "Antibodies bind to antigens on pathogens. Antitoxins neutralise toxins produced by infecting pathogens.",
                                    "isCorrect": False
                                },
                                {
                                    "id": "3",
                                    "text": "Phagocytes",
                                    "response": "Antibodies bind to antigens on pathogens. Phagocytes are white blood cells that engulf pathogens.",
                                    "isCorrect": False
                                }]
                            }],

                "zxr7ng8" : [{
                                "id": "5",
                                "text": "HIV/AIDS is what type of pathogen?",
                                "options": [{
                                    "id": "1",
                                    "text": "A virus",
                                    "response": "HIV/AIDS is a virus.",
                                    "isCorrect": True
                                },
                                {
                                    "id": "2",
                                    "text": "A fungus",
                                    "response": "HIV/AIDS is a virus. Athlete's foot is an example of a disease caused by a fungus.",
                                    "isCorrect": False
                                },
                                {
                                    "id": "3",
                                    "text": "A bacterium",
                                    "response": "HIV/AIDS is a virus. Salmonella is an example of a disease caused by a bacterium.",
                                    "isCorrect": False
                                }]
                            }],

                "z3tgw6f" : [{
                                "id": "6",
                                "text": "What treatment is used for rose black spot?",
                                "options": [{
                                    "id": "1",
                                    "text": "Herbicides",
                                    "response": "Fungicides are used to treat rose black spot. Herbicides kill plant pests/weeds.",
                                    "isCorrect": "False"
                                },
                                {
                                    "id": "2",
                                    "text": "Fungicides",
                                    "response": "Fungicides are used to treat rose black spot.",
                                    "isCorrect": "True"
                                },
                                {
                                    "id": "3",
                                    "text": "Insecticides",
                                    "response": "Fungicides are used to treat rose black spot. Insecticides kill insects.",
                                    "isCorrect": "False"
                                }]
                            }],

                "z8fkmsg": [{
                                "id": "7",
                                "text": "What is an antigen?",
                                "options": [{
                                    "id": "1",
                                    "text": "A chemical produced by the white blood cells",
                                    "response": "An antigen is a chemical on the surface of a pathogen. They stimulate the white blood cells to produce antibodies.  Antibodies are produced by the white blood cells.",
                                    "isCorrect": "False"
                                },
                                {
                                    "id": "2",
                                    "text": "A chemical on the surface of the pathogen",
                                    "response": "An antigen is a chemical on the surface of a pathogen.",
                                    "isCorrect": "True"
                                },
                                {
                                    "id": "3",
                                    "text": "A mircobe that causes a disease",
                                    "response": "An antigen is a chemical on the surface of a pathogen. A pathogen is a disease-causing microbe.",
                                    "isCorrect": "False"
                                }]
                            }],
}
