__author__ = "Regenplatz"
__version__ = "1.0.0"


import pandas as pd
import numpy as np
from datetime import datetime


## months
l_months = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]
d_months = {i: {"short": month[:3], "long": month} for i, month in enumerate(l_months, 1)}

## weekdays
l_weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
d_weekdays = {i: {"short": weekday[:3], "long": weekday} for i, weekday in enumerate(l_weekdays, 1)}
d_weekend = {k: 1 if k in [6, 7] else 0 for k, v in d_weekdays.items()}


def create_calendar(s_date_start: str, s_date_end: str) -> pd.DataFrame:
    """
    Create a dataframe for dates within the given range. Each date is in a separate row.
    Add further columns for date-specific information, e.g. year, month, day, weekday, etc.
    :param s_date_start: start date (as string)
    :param s_date_end: start date (as string)
    :return: dataframe with dates for the given date range, containing further date-specific information.
    """
    ## create dataframe
    df = pd.date_range(start=s_date_start, end=s_date_end, freq="D").to_frame(name='date_')
    df["i_year"] = df["date_"].dt.year
    df["i_month"] = df["date_"].dt.month
    df["s_month_short"] = df["i_month"].map({k: v["short"] for k, v in d_months.items()})
    df["s_month_long"] = df["i_month"].map({k: v["long"] for k, v in d_months.items()})
    df["i_week"] = df["date_"].dt.isocalendar().week
    df["i_day_of_month"] = df["date_"].dt.day
    df["i_day_of_week_iso"] = df["date_"].dt.weekday + 1
    df["s_day_of_week_short"] = df["i_day_of_week_iso"].map({k: v["short"] for k, v in d_weekdays.items()})
    df["s_day_of_week_long"] = df["i_day_of_week_iso"].map({k: v["long"] for k, v in d_weekdays.items()})
    df["b_weekend"] = df["i_day_of_week_iso"].map(d_weekend)

    ## set date as index
    l_idx_datetime = df.index
    df["date"] = [datetime.date(idx) for idx in l_idx_datetime]
    df.set_index("date", inplace=True, drop=True)

    return df


def evaluate_workingday(df: pd.DataFrame) -> pd.DataFrame:
    """
    Evaluate working day (not weekend and not holiday). Create separate column.
    :param df: calendar dataframe, to which an additional column for working day is added.
    :return: calendar dataframe, containing an additional column for working day
    """
    cond = (df["b_weekend"] != 1) & (pd.isna(df["holiday"]))
    df["b_workingday"] = 0
    df["b_workingday"] = np.where(cond, 1, 0)
    return df
