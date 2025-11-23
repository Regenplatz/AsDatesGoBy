__author__ = "Regenplatz"
__version__ = "1.0.0"


import pandas as pd
from datetime import datetime, date
from typing import Dict
from pymeeus.Sun import Sun


d_season_starts_meteorological = { ## -MM-dd
    "Beginning of Spring (meteorological)": "-03-01",
    "Beginning of Summer (meteorological)": "-06-01",
    "Beginning of Autumn (meteorological)": "-09-01",
    "Beginning of Winter (meteorological)": "-12-01"
}


def evaluate_dates_seasonstarts_for_years(l_years: list) -> Dict[date, str]:
    """
    Evaluate meteorological and astronomical beginnings of seasons for given years.
    :param l_years: years of interest
    :return: dictionary containing dates of season starts as keys and info on season type as values
    """
    d_dates = {}
    for i_year in l_years:

        ## meteorological season start dates
        for k, v in d_season_starts_meteorological.items():
            date_ = datetime.strptime(f"{i_year}{v}", "%Y-%m-%d").date()
            d_dates[date_] = k

        ## astronomical season start dates
        l_target = ["spring", "summer", "autumn", "winter"]
        for target in l_target:
            epoch = Sun.get_equinox_solstice(i_year, target=target)
            date_ = datetime.strptime(f"{epoch.get_full_date()[0]}-{epoch.get_full_date()[1]}-{epoch.get_full_date()[2]}", "%Y-%m-%d").date()
            d_dates[date_] = f"Beginning of {target} (astronomical)"
    return d_dates


def evaluate_dates_seasonstarts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create column for season starts in calendar dataframe.
    :param df: calendar dataframe
    :return: calendar dataframe, containing a column for season starts
    """
    ## evaluate holidays for all years in calendar dataframe
    l_years = df["i_year"].unique().tolist()
    d_seasonstarts = evaluate_dates_seasonstarts_for_years(l_years)
    df["beginning_of_season"] = df["date_"].map(d_seasonstarts)
    return df
