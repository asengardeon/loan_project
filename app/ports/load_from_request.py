from singleton_decorator import singleton

from app.loan.loan_data import Loan


@singleton
class LoanFromArgRequest:
    def execute(self, args) -> Loan:
        self.amount = args.get('amount')
        self.term = args.get('term')
        self.credit_score = args.get('credit_score')
        self.vehicle_year = args.get('vehicle_year')
        self.vehicle_mileage = args.get('vehicle_mileage')
        return Loan(amount=self.amount, term=self.term, credit_score=self.credit_score, vehicle_year=self.vehicle_year, vehicle_mileage=self.vehicle_year)





