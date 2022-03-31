from main import app

client = app.test_client()


def test_apr_request():
    result = client.get("/apr",  query_string=dict(amount= 10000, term=36, credit_score=700, vehicle_year=2014,
                                                   vehicle_mileage=50000))
    assert result.data.strip() == b'5.75'
    assert result.status_code == 201