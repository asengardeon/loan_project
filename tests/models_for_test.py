class BaseRate:
    term: int
    score: int
    percent: float

    def __init__(self, term, score, percent) -> None:
        super().__init__()
        self.term = term
        self.score = score
        self.percent = percent


