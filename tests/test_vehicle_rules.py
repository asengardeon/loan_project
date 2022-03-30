from app.loan.rules import Rules

rules = Rules()


def test_increment_base_rate_by_year():
    year = 2014
    value = rules._increment_by_year(year)
    assert value == 1.0, f"Vehicle before 2015 should increment base rate. Year was {year}"


def test_not_increment_base_rate_by_year():
    year = 2015
    value = rules._increment_by_year(year)
    assert value == 0.0, f"Only Vehicle before 2015 should increment base rate. Year was {year}"


def test_increment_base_rate_by_mileage():
    mileage = 100001
    value = rules._increment_by_mileage(mileage)
    assert value == 2.0, f"Vehicle above 100k mileage should increment base rate. Mileage was {mileage}"


def test_increment_base_rate_by_mileage_on_limit():
    mileage = 100000
    value = rules._increment_by_mileage(mileage)
    assert value == 2.0, f"Vehicle above 100k mileage should increment base rate. Mileage was {mileage}"



def test_not_increment_base_rate_by_mileage():
    mileage = 99999
    value = rules._increment_by_year(mileage)
    assert value == 0.0, f"Only Vehicle above 100k mileage should increment base rate. Mileage was {mileage}"


def test_vehicle_data_increment_year():
    year = 2014
    mileage = 99999
    value = rules.increment_percent_by_vehicle_data(year, mileage)
    assert value == 1.0, f"Vehicle before 2015 should increment base rate. Year was {year}"


def test_vehicle_data_increment_mileage():
    year = 2015
    mileage = 100001
    value = rules.increment_percent_by_vehicle_data(year, mileage)
    assert value == 2.0, f"Vehicle above 100k mileage should increment base rate. Year was {mileage}"


def test_vehicle_data_increment_mileage_and_year():
    year = 2014
    mileage = 100001
    value = rules.increment_percent_by_vehicle_data(year, mileage)
    assert value == 3.0, f"Vehicle above 100k mileage and year before 2015 should increment base rate. Year was {mileage}"

