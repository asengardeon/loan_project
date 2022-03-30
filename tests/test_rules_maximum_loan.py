from app.loan.exceptions.invalid_score_value import InvalidScoreValueException
from app.loan.rules import Rules

rules = Rules()

def test_maximum_loan_score_700_value_invalid():
    amount = 100001
    credit_score = 700
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == False, f"Params used: amount={amount}, credit_score={credit_score}"


def test_maximum_loan_score_700_value_valid_on_limit():
    amount = 100000
    credit_score = 700
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == True, f"Params used: amount={amount}, credit_score={credit_score}"


def test_maximum_loan_score_above_700_value_valid_on_limit():
    amount = 100000
    credit_score = 730
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == True, f"Params used: amount={amount}, credit_score={credit_score}"


def test_maximum_loan_score_700_value_valid():
    amount = 90000
    credit_score = 730
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == True, f"Params used: amount={amount}, credit_score={credit_score}"



def test_maximum_loan_score_600_value_invalid():
    amount = 50001
    credit_score = 599
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == False, f"Params used: amount={amount}, credit_score={credit_score}"


def test_maximum_loan_score_600_value_valid_on_limit():
    amount = 50000
    credit_score = 599
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == True, f"Params used: amount={amount}, credit_score={credit_score}"


def test_maximum_loan_score_below_600_value_valid_on_limit():
    amount = 50000
    credit_score = 500
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == True, f"Params used: amount={amount}, credit_score={credit_score}"


def test_maximum_loan_score_600_value_valid():
    amount = 45000
    credit_score = 599
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == True, f"Params used: amount={amount}, credit_score={credit_score}"



def test_maximum_loan_score_between_600_699_value_invalid():
    amount = 75001
    credit_score = 600
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == False, f"Params used: amount={amount}, credit_score={credit_score}"


def test_maximum_loan_score_between_600_699_value_valid_on_limit():
    amount = 75000
    credit_score = 600
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == True, f"Params used: amount={amount}, credit_score={credit_score}"


def test_maximum_loan_score_between_600_699_value_valid():
    amount = 60000
    credit_score = 630
    valid = rules._validate_loan_by_score(credit_score, amount)
    assert valid == True, f"Params used: amount={amount}, credit_score={credit_score}"


def test_invalid_score_exception():
    amount = 60000
    credit_score = -1
    try:
        rules._validate_loan_by_score(credit_score, amount)
        value = False
    except InvalidScoreValueException:
        value = True
    assert value == True, "Validation should throws exceptions to invalid score"
