from datetime import date


class Loan:
    amount: float
    term: int
    credit_score: int
    vehicle_year: date
    vehicle_mileage: int

    def __init__(self, amount, term, credit_score, vehicle_year, vehicle_mileage) -> None:
        super().__init__()
        self.amount = amount
        self.term = term
        self.credit_score = credit_score
        self.vehicle_year = vehicle_year
        self.vehicle_mileage = vehicle_mileage




