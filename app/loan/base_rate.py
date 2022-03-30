from typing import Dict

from app.loan import term_up_48, score_up_699, term_up_60, score_up_599, term_up_36, score_up_700


class BaseRate:

    configs = {}

    def _fill_configs(self):
        self.configs = { term_up_48: {score_up_699: 0.0}, term_up_60:{score_up_599: 0.0}, term_up_36:{score_up_700: 0.0} }
        self.configs[term_up_36][score_up_700] = 4.75
        self.configs[term_up_48][score_up_700] = 5
        self.configs[term_up_60][score_up_700] = 5.5
        self.configs[term_up_36][score_up_699] = 5.75
        self.configs[term_up_48][score_up_699] = 6
        self.configs[term_up_60][score_up_699] = 6.65
        self.configs[term_up_36][score_up_599] = 12.75
        self.configs[term_up_48][score_up_599] = 13.25
        self.configs[term_up_60][score_up_599] = None


    def __init__(self) -> None:
        super().__init__()
        self._fill_configs()


    def _filter_term(self, term)-> Dict:
        if term <=36:
            return self.configs[term_up_36]
        elif term <= 48:
            return self.configs[term_up_48]
        return self.configs[term_up_60]


    def _filter_score(self, score: int)-> float:
        if score < 600:
            return score_up_599
        elif score < 700:
            return score_up_699
        return score_up_700


    def execute(self, term, score):
        value = self._filter_term(term)[self._filter_score(score)]
        return value
