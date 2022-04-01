import http

from main import app

APR_ENDPOINT = "/api/v1/apr"

client = app.test_client()


def test_apr_request():
    result = client.get(APR_ENDPOINT, query_string=dict(amount= 10000, term=36, credit_score=700, vehicle_year=2014,
                                               vehicle_mileage=50000))
    assert result.data.strip() == b'5.75'
    assert result.status_code == http.client.OK


def test_apr_request_amount_missed():
    result = client.get(APR_ENDPOINT,  query_string=dict(term=36, credit_score=700, vehicle_year=2014,
                                                   vehicle_mileage=50000))
    assert str(result.data).find("Param amount is missed") > -1
    assert result.status_code == http.client.BAD_REQUEST

def test_apr_request_term_missed():
    result = client.get(APR_ENDPOINT,  query_string=dict(amount= 10000, credit_score=700, vehicle_year=2014,
                                                   vehicle_mileage=50000))
    assert str(result.data).find("Param term is missed") > -1
    assert result.status_code == http.client.BAD_REQUEST

def test_apr_request_credit_score_missed():
    result = client.get(APR_ENDPOINT,  query_string=dict(amount= 10000, term=36, vehicle_year=2014,
                                                   vehicle_mileage=50000))
    assert str(result.data).find("Param credit_score is missed") > -1
    assert result.status_code == http.client.BAD_REQUEST

def test_apr_request_vehicle_year_missed():
    result = client.get(APR_ENDPOINT,  query_string=dict(amount= 10000, term=36, credit_score=700,
                                                   vehicle_mileage=50000))
    assert str(result.data).find("Param vehicle_year is missed") > -1
    assert result.status_code == http.client.BAD_REQUEST

def test_apr_request_vehicle_mileage_missed():
    result = client.get(APR_ENDPOINT,  query_string=dict(amount= 10000, term=36, credit_score=700,
                                                   vehicle_year=2014))
    assert str(result.data).find("Param vehicle_mileage is missed") > -1
    assert result.status_code == http.client.BAD_REQUEST

def test_apr_request_term_invalid_negative():
    result = client.get(APR_ENDPOINT,  query_string=dict(amount= 10000, term=-1, credit_score=700, vehicle_year=2014,
                                                   vehicle_mileage=50000))
    assert str(result.data).find("Invalid Term") > -1
    assert result.status_code == http.client.BAD_REQUEST

def test_apr_request_term_invalid_upper_60():
    result = client.get(APR_ENDPOINT,  query_string=dict(amount= 10000, term=61, credit_score=700, vehicle_year=2014,
                                                   vehicle_mileage=50000))
    assert str(result.data).find("Invalid Term") > -1
    assert result.status_code == http.client.BAD_REQUEST


def test_apr_request_score_invalid():
    result = client.get(APR_ENDPOINT,  query_string=dict(amount=10000, term=36, credit_score=-1, vehicle_year=2014,
                                                   vehicle_mileage=50000))
    assert str(result.data).find("Invalid score") > -1
    assert result.status_code == http.client.BAD_REQUEST

