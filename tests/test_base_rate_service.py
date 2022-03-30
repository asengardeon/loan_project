import pytest as pytest

from app.services.base_rate import BaseRateService
from tests.models_for_test import BaseRate

testdata_score_up_700 = [
    BaseRate(term=1, score=700, percent=4.75),
    BaseRate(term=24, score=700, percent=4.75),
    BaseRate(term=36, score=700, percent=4.75),
    BaseRate(term=44, score=700, percent=5),
    BaseRate(term=48, score=700, percent=5),
    BaseRate(term=55, score=700, percent=5.5),
    BaseRate(term=60, score=700, percent=5.5),
    BaseRate(term=1, score=701, percent=4.75 ),
    BaseRate(term=36, score=701, percent=4.75),
    BaseRate(term=48, score=701, percent=5),
    BaseRate(term=60, score=701, percent=5.5)
]

testdata_score_lower_600 = [
    BaseRate(term=1, score=599, percent=12.75),
    BaseRate(term=24, score=599, percent=12.75),
    BaseRate(term=36, score=599, percent=12.75),
    BaseRate(term=44, score=599, percent=13.25),
    BaseRate(term=48, score=599, percent=13.25),
    BaseRate(term=55, score=599, percent=None),
    BaseRate(term=60, score=599, percent=None),
    BaseRate(term=1, score=500, percent=12.75),
    BaseRate(term=36, score=500, percent=12.75),
    BaseRate(term=48, score=0, percent=13.25),
    BaseRate(term=60, score=0, percent=None)
]

testdata_score_higher_599_lower_700 = [
    BaseRate(term=1, score=600, percent=5.75),
    BaseRate(term=24, score=600, percent=5.75),
    BaseRate(term=36, score=600, percent=5.75),
    BaseRate(term=44, score=600, percent=6),
    BaseRate(term=48, score=600, percent=6),
    BaseRate(term=55, score=600, percent=6.65),
    BaseRate(term=60, score=600, percent=6.65),
    BaseRate(term=1, score=650, percent=5.75),
    BaseRate(term=36, score=650, percent=5.75),
    BaseRate(term=48, score=699, percent=6),
    BaseRate(term=60, score=699, percent=6.65)
]


service = BaseRateService()

@pytest.mark.parametrize("base_test", testdata_score_up_700)
def test_score_up_700(base_test: BaseRate):
    result = service.execute(base_test.term, base_test.score)
    assert result == base_test.percent, f"Percent with term={base_test.term} and score={base_test.score} has failed"


@pytest.mark.parametrize("base_test", testdata_score_lower_600)
def test_score_lower_600(base_test: BaseRate):
    result = service.execute(base_test.term, base_test.score)
    assert result == base_test.percent, f"Percent with term={base_test.term} and score={base_test.score} has failed"


@pytest.mark.parametrize("base_test", testdata_score_higher_599_lower_700)
def test_score_higher_600_lower_700(base_test: BaseRate):
    result = service.execute(base_test.term, base_test.score)
    assert result == base_test.percent, f"Percent with term={base_test.term} and score={base_test.score} has failed"