import pytest
from unittest import mock
from date import Date, DateValidationError, DateStamp
import freezegun


@pytest.fixture
def date():
    return Date()


@pytest.mark.parametrize(
    "year, expected_result",
    [
        (2001, False),
        (2000, True),
        (1900, False),
        (2004, True),
        (2008, True),
        (2100, False),
        (2400, True),
    ]
)
def test_is_leap_year(year, expected_result):
    assert Date.is_leap_year(year) == expected_result


@pytest.mark.parametrize(
    "input_values, expected_day, expected_month, expected_year, expected_era",
    [
        (['1.1.1'], 1, 1, 1, False),
        (["1.1.0001", "1.1.1"], 1, 1, 1, False),
        (["1.1.2023", "1.1.1"], 1, 1, 2023, False),
        (["1.1.-2022", "1.1.1"], 1, 1, 2022, True),
    ]
)
def test_input_date(input_values, expected_day, expected_month, expected_year, expected_era):
    with mock.patch('builtins.input', side_effect=input_values):
        d = Date()
        d.input_date()
        assert d.day == expected_day
        assert d.month == expected_month
        assert d.year == expected_year
        assert d.before_common_era == expected_era


@pytest.mark.parametrize(
    "month, year, expected_days",
    [
        (2, 2000, 29),
        (2, 2001, 28),
        (3, 2000, 31),
        (4, 2001, 30),
        (5, 2000, 31),
        (6, 2001, 30),
        (7, 2000, 31),
        (8, 2001, 31),
        (9, 2000, 30),
        (10, 2001, 31),
        (11, 2000, 30),
        (12, 2001, 31),
    ]
)
def test_days_in_month(date, month, year, expected_days):
    date.month = month
    date.year = year
    assert date.days_in_month() == expected_days


@pytest.mark.parametrize(
    "day, month, year, error_message",
    [
        (32, 1, 1, "день"),
        (15, 13, 1, "месяц"),
        (1, 1, 0, "Год"),
    ]
)
def test_validate_date(date, day, month, year, error_message):
    date.day = day
    date.month = month
    date.year = year
    with pytest.raises(DateValidationError, match=error_message):
        date.validate_date()


def test_add_days(date):
    date.day = 31
    date.month = 12
    date.add_days(1)
    assert date.day == 1
    assert date.month == 1
    assert date.year == 2


def test_subtract_days(date):
    date.day = 1
    date.month = 1
    date.year = 2
    date.subtract_days(1)
    assert date.day == 31
    assert date.month == 12
    assert date.year == 1


def test_days_from_epoch(date):
    date.day = 1
    date.month = 1
    date.year = 2
    assert date.days_from_epoch() == 365


def test_adjust_days(date):
    date.day = 1
    date.month = 1
    date.year = 2000
    date.adjust_days(1)
    assert date.day == 2
    date.adjust_days(-1)
    assert date.day == 1


@pytest.mark.parametrize(
    "freeze_date, expected_day, expected_month, expected_year",
    [
        ('0001-1-1', 1, 1, 1),
        ("1941-6-22", 22, 6, 1941),
        ("2023-1-2", 2, 1, 2023),
        ("2022-2-28", 28, 2, 2022)
    ]
)
def test_init(freeze_date, expected_day, expected_month, expected_year):
    with freezegun.freeze_time(freeze_date):
        d = DateStamp()
    assert d.day == expected_day
    assert d.month == expected_month
    assert d.year == expected_year
    assert d.before_common_era is False
