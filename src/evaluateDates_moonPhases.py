__author__ = "Regenplatz"
__version__ = "1.0.0"


import pandas as pd
import pytz
from datetime import datetime, timedelta


def evaluate_dates_moonphases(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a column for moon phase information (Full Moon, New Moon) to the calendar dataframe.
    :param df: calendar dataframe, to which a column for moon phase information should be added
    :return: calendar dataframe with moon phase information
    """
    ## define timezones
    tz_utc = pytz.timezone("UTC")
    tz_cet = pytz.timezone("Europe/Berlin")

    meanLunationPeriod = timedelta(days=29, hours=12, minutes=44, seconds=3)
    dt_2000_1stNewMoon = datetime(2000, 1, 6, 18, 14, 0, tzinfo=tz_utc)
    d_moon = {
        "newMoon_utc": [dt_2000_1stNewMoon],
        "newMoon_cet": [dt_2000_1stNewMoon.astimezone(tz_cet)],
        "fullMoon_utc": [dt_2000_1stNewMoon + (meanLunationPeriod / 2)],
        "fullMoon_cet":  [(dt_2000_1stNewMoon + (meanLunationPeriod / 2)).astimezone(tz_cet)]
    }

    dt_start = min(df["date_"]).to_pydatetime().astimezone(pytz.timezone("Europe/Berlin"))
    dt_end = max(df["date_"]).to_pydatetime().astimezone(pytz.timezone("Europe/Berlin"))
    for k, v in d_moon.items():
        dt_moon = v[0]
        d_moon[k] = [datetime.date(v[0])]
        while dt_moon <= dt_end:
            dt_moon += meanLunationPeriod
            v.append(dt_moon)
        d_moon[k] = [datetime.date(elem) for elem in v if (elem >= dt_start) and (elem <= dt_end)]

    for date_ in d_moon["fullMoon_cet"]:
        df.loc[date_, "s_moonphase"] = "Full Moon"
    for date_ in d_moon["newMoon_cet"]:
        df.loc[date_, "s_moonphase"] = "New Moon"

    return df
