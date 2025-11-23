__author__ = "Regenplatz"
__version__ = "1.0.0"


import pandas as pd
from datetime import datetime, date, timedelta
from typing import List, Dict


## fixed holidays
d_holidays = { ## -month-day
    "New Year's Day": "-01-01",
    "St Berchtold's Day": "-01-02",
    "National Holiday": "-08-01",
    "All Saints Day": "-11-01",
    "Christmas Eve": "-12-24",
    "Christmas Day": "-12-25",
    "Boxing Day": "-12-26",
    "New Year's Eve": "-12-31",
}


def evaluate_fixed_holidays(i_year: int) -> Dict[date, str]:
    """
    Evaluate dates of fixed holidays.
    E.g. Christmas Eve is on 24th of December every year.
    :param i_year: year of interest
    :return: dictionary containing all fixed holidays within a given year (holiday name as keys, dates as values)
    """
    return {datetime.strptime(f"{i_year}{v}", "%Y-%m-%d").date(): k for k, v in d_holidays.items()}


def evaluate_easter_date(i_year: int) -> date:
    """
    Formula taken from: https://en.wikipedia.org/wiki/Date_of_Easter
    :param i_year: year of interest
    :return: date of Easter day for the given year
    """
    a = i_year % 19
    b = i_year % 4
    c = i_year % 7
    k = i_year // 100
    p = (13 + 8 * k) // 25
    q = k // 4
    M = (15 - p + k - q) % 30
    N = (4 + k - q) % 7
    d = (19 * a + M) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + N) % 7
    easter_march = d + e + 22
    easter_april = d + e - 9

    if easter_march <= 31:
        s_easter = f"{i_year}-03-{easter_march}"
    else:
        if (easter_april == 25) and (d == 8) and (e == 6) and (a < 10):
            s_easter = f"{i_year}-04-18"
        elif (easter_april == 26) and (d == 29) and (e == 6):
            s_easter = f"{i_year}-04-19"
        else:
            s_easter = f"{i_year}-04-{easter_april}"

    return datetime.strptime(s_easter, "%Y-%m-%d").date()


def evaluate_dates_holiday_for_years(l_years: List[int]) -> Dict[str, date]:
    """
    Evaluate all holidays for the given years. Start with all fixed holidays. Expand result dictionary
    with floating holidays - which are mostly related to Easter date.
    :param l_years: list of years of interest
    :return: dictionary containing all holidays within a given year (holiday name as keys, dates as values)
    """
    d_holidays = {}
    for i_year in l_years:

        ## evaluate fixed holiday dates for a given year
        d_fixed_holidays_for_year = evaluate_fixed_holidays(i_year)
        d_holidays.update(d_fixed_holidays_for_year)

        ## evaluate Easter
        easter = evaluate_easter_date(i_year=i_year)
        d_holidays[easter] = "Easter"

        ## Easter Monday (= Easter + 1d)
        d_holidays[easter + timedelta(days=1)] = "Easter Monday"

        ## Good Friday (= Easter - 2d)
        d_holidays[easter + timedelta(days=-2)] = "Good Friday"

        ## Good Tuesday (= Easter - 40d)
        d_holidays[easter + timedelta(days=-40)] = "Good Tuesday"

        ## Ash Wednesday (= Easter - 39d)
        d_holidays[easter + timedelta(days=-39)] = "Ash Wednesday"

        ## Ascension Day (= Easter + 40d)
        d_holidays[easter + timedelta(days=40)] = "Ascension Day"

        ## Pentecost (= Easter + 49d)
        d_holidays[easter + timedelta(days=49)] = "Pentecost"

        ## Whit Monday (= Easter + 50d)
        d_holidays[easter + timedelta(days=50)] = "Whit Monday"

    return d_holidays


def evaluate_dates_holidays(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create column for holidays in calendar dataframe.
    :param df: calendar dataframe
    :return: calendar dataframe, containing a column for holidays
    """
    l_years = df["i_year"].unique().tolist()
    d_holidays = evaluate_dates_holiday_for_years(l_years)
    df["holiday"] = df["date_"].map(d_holidays)
    return df

