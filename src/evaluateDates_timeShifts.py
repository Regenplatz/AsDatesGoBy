__author__ = "Regenplatz"
__version__ = "1.0.0"


import pandas as pd


def evaluate_dates_timeshifts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Begin summer time: last Sunday in March
    Begin winter time: last Sunday in October
    :param df: calendar dataframe containing date time specifics. To be extended by a column for time shift information.
    :return: calendar dataframe containing an additional column for time shift information.
    """
    d_dates = {}
    l_years = list(df["i_year"].unique())
    for year in l_years:

        ## summertime
        condition_summertime = (df["i_year"] == year) & (df["i_month"] == 3) & (df["s_day_of_week_short"] == "Sun")
        s_timeshift_st = df.loc[condition_summertime, "date_"]
        if not s_timeshift_st.empty:
            if year in d_dates:
                d_dates[year]["Begin Summer Time"] = pd.to_datetime(s_timeshift_st.iloc[-1]).date()
            else:
                d_dates[year] = {"Begin Summer Time": pd.to_datetime(s_timeshift_st.iloc[-1]).date()}

        ## wintertime
        condition_wintertime = (df["i_year"] == year) & (df["i_month"] == 10) & (df["s_day_of_week_short"] == "Sun")
        s_timeshift_wt = df.loc[condition_wintertime, "date_"]
        if not s_timeshift_wt.empty:
            if year in d_dates:
                d_dates[year]["Begin Winter Time"] = pd.to_datetime(s_timeshift_wt.values[-1]).date()
            else:
                d_dates[year] = {"Begin Winter Time": pd.to_datetime(s_timeshift_wt.values[-1]).date()}

    for year, time_shift in d_dates.items():
        for shift_type, date_ in time_shift.items():
            df.loc[date_, "s_timeShift"] = shift_type

    return df
