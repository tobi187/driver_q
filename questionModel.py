# import dataclasses


# @dataclasses.dataclass
# class Questions:
#     question: str
#     # list or dict or else ??
#     answer_options: list[str]
#     correct_answer: str  # or index
#     user_answer: str
#     explanation: str


class Questions:
    def __init__(self, question, answer_options, correct_answer, user_answer, explanation) -> None:
        self.question = question  # frage
        self.answer_options = answer_options  # liste mit 4 Antwortmöglichkeiten
        self.correct_answer = correct_answer  # a,b,c oder d
        self.explanation = explanation  # entweder leerer text oder Erklärung
        # Erst leer lassen und später die Antwort vom User eintragen
        self.user_answer = user_answer  # a,b,c oder d
