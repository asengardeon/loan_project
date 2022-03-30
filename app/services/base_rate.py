from app.loan.base_rate import BaseRate


class BaseRateService:
    def execute(self, term, score):
        rate = BaseRate()
        value = rate.execute(term, score)
        return value