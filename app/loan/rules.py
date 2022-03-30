from app.loan import term_up_48, term_up_36, score_up_700, score_up_699, term_up_60, score_up_599
from app.loan.exceptions.invalid_score_value import InvalidScoreValueException
from app.loan.exceptions.invalid_term import InvalidTermValueException
from app.loan.loan_data import Loan


class Rules:
    minimum_loan = {}
    maximum_loan = {}

    def _fill_configs(self):
        self.minimum_loan = {term_up_36: 5000, term_up_48: 10000, term_up_60: 15000}
        self.maximum_loan = {score_up_599: 50000, score_up_699: 75000, score_up_700: 100000}

    def __init__(self) -> None:
        super().__init__()
        self._fill_configs()

    def _validate_term(self, term, amount):
        if term <= term_up_36:
            internal_term = term_up_36
        elif term <= term_up_48:
            internal_term = term_up_48
        elif term <= 60:
            internal_term = term_up_60
        else:
            raise InvalidTermValueException(f"The term {term} is not a valid value")
        return self.minimum_loan[internal_term] <= amount

    def _validate_loan_by_score(self, score, amount):
        if 0 < score < score_up_699:
            internal_score = score_up_599
        elif score_up_699 <= score < score_up_700:
            internal_score = score_up_699
        elif score >= score_up_700:
            internal_score = score_up_700
        else:
            raise InvalidScoreValueException(f"The score {score} is not a valid value")
        return self.maximum_loan[internal_score] >= amount

    def _increment_by_year(self, year):
        if year < 2015:
            return 1.0
        return 0.0

    def _increment_by_mileage(self, mileage):
        if mileage >= 100000:
            return 2.0
        return 0.0


    def validate_minimum_maximum_values(self, loan: Loan):
        valid_minimum_loan = self._validate_term(loan.term, loan.amount)
        valid_maximum_loan = self._validate_loan_by_score(loan.credit_score, loan.amount)
        return valid_minimum_loan and valid_maximum_loan

    def increment_percent_by_vehicle_data(self, year, mileage):
        return self._increment_by_year(year) + self._increment_by_mileage(mileage)

