import dataclasses


@dataclasses.dataclass
class Questions:
    # id: int
    question: str
    # list or dict or else ??
    answer_options: list[str]
    correct_answer: str  # or index
    user_answer: str
    explanation: str
