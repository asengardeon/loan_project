from singleton_decorator import singleton

from app.loan.exceptions.param_missed import ParamMissedException
from app.loan.loan_data import Loan


@singleton
class LoanFromArgRequest:


    def _validate_atributtes(self, args):
        argamount = args.get('amount')
        if argamount is not None:
            self.amount = float(argamount)
        else:
            raise ParamMissedException("amount")
        argterm = args.get('term')
        if argterm is not None:
            self.term = float(argterm)
        else:
            raise ParamMissedException("term")
        argcredit_score = args.get('credit_score')
        if argcredit_score is not None:
            self.credit_score = float(argcredit_score)
        else:
            raise ParamMissedException("credit_score")
        argvehicle_year = args.get('vehicle_year')
        if argvehicle_year is not None:
            self.vehicle_year = float(argvehicle_year)
        else:
            raise ParamMissedException("vehicle_year")
        argvehicle_mileage = args.get('vehicle_mileage')
        if argvehicle_mileage is not None:
            self.vehicle_mileage = float(argvehicle_mileage)
        else:
            raise ParamMissedException("vehicle_mileage")


    def execute(self, args) -> Loan:
        self._validate_atributtes(args)

        return Loan(amount=self.amount, term=self.term, credit_score=self.credit_score, vehicle_year=self.vehicle_year, vehicle_mileage=self.vehicle_year)







