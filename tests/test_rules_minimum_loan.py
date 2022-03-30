from app.loan.exceptions.invalid_term import InvalidTermValueException
from app.loan.loan_data import Loan
from app.loan.rules import Rules

rules = Rules()


def test_minimum_loan_term_up_to_36_value_invalid():
    amount = 4009
    term = 36
    valid = rules._validate_term(term, amount)
    assert valid == False, f"Params used: amount={amount}, term={term}"


def test_minimum_loan_term_up_to_36_value_valid_on_limit():
    amount = 5000
    term = 36
    valid = rules._validate_term(term, amount)
    assert valid == True, f"Params used: amount={amount}, term={term}"


def test_minimum_loan_term_up_to_36_value_valid():
    amount = 5001
    term = 36
    valid = rules._validate_term(term, amount)
    assert valid == True, f"Params used: amount={amount}, term={term}"


def test_minimum_loan_term_up_to_48_value_invalid():
    amount = 9999
    term = 48
    valid = rules._validate_term(term, amount)
    assert valid == False, f"Params used: amount={amount}, term={term}"


def test_minimum_loan_term_up_to_48_value_valid_on_limit():
    amount = 10000
    term = 48
    valid = rules._validate_term(term, amount)
    assert valid == True, f"Params used: amount={amount}, term={term}"


def test_minimum_loan_term_up_to_48_value_valid():
    amount = 10001
    term = 48
    valid = rules._validate_term(term, amount)
    assert valid == True, f"Params used: amount={amount}, term={term}"


def test_minimum_loan_term_up_to_60_value_invalid():
    amount = 14999
    term = 60
    valid = rules._validate_term(term, amount)
    assert valid == False, f"Params used: amount={amount}, term={term}"


def test_minimum_loan_term_up_to_60_value_valid_on_limit():
    amount = 15000
    term = 60
    valid = rules._validate_term(term, amount)
    assert valid == True, f"Params used: amount={amount}, term={term}"


def test_minimum_loan_term_up_to_60_value_valid():
    amount = 15001
    term = 60
    valid = rules._validate_term(term, amount)
    assert valid == True, f"Params used: amount={amount}, term={term}"


def test_invalid_score_exception():
    amount = 60000
    term = 76
    try:
        rules._validate_term(term, amount)
        value = False
    except InvalidTermValueException:
        value = True
    assert value == True, "Validation should throws exceptions to invalid term"
