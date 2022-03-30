from singleton_decorator import singleton
from app.loan.exceptions.not_valid_loan import NotValidLoanException
from app.loan.loan_data import Loan
from app.loan.rules import Rules
from app.services.base_rate import BaseRateService


@singleton
class LoanService:

    def __init__(self) -> None:
        super().__init__()
        self.rules = Rules()
        self.base_rate = BaseRateService()

    def get_loan_percent(self, desire: Loan):
        validated = self.rules.validate_minimum_maximum_values(desire)
        if not validated:
            raise NotValidLoanException()

        percent = self.base_rate.execute(desire.term, desire.amount)
        percent += self.rules.increment_percent_by_vehicle_data(desire.vehicle_year, desire.vehicle_mileage)
        return percent
