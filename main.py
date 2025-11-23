__author__ = "Regenplatz"
__version__ = "1.0.0"


from src import (
    createCalendar as cal,
    evaluateDates_holidays as hld,
    evaluateDates_moonPhases as mop,
    evaluateDates_seasonStarts as sst,
    evaluateDates_timeShifts as tsh
)


s_date_start = "2025-01-01"
s_date_end = "2029-12-31"
df = cal.create_calendar(s_date_start=s_date_start, s_date_end=s_date_end)
df = hld.evaluate_dates_holidays(df=df)
df = cal.evaluate_workingday(df=df)
df = tsh.evaluate_dates_timeshifts(df=df)
df = mop.evaluate_dates_moonphases(df=df)
df = sst.evaluate_dates_seasonstarts(df=df)
