
from datetime import datetime, timedelta
import pandas as pd
from src import (
    createCalendar as cal,
    evaluateDates_holidays as hld,
    evaluateDates_moonPhases as mop,
    evaluateDates_seasonStarts as sst,
    evaluateDates_timeShifts as tsh
)


##### LOAD DATA ###############################################################################################

## create dataframe that needs to be tested
s_date_start = "2025-01-01"
s_date_end = "2029-12-31"
df = cal.create_calendar(s_date_start=s_date_start, s_date_end=s_date_end)
df = hld.evaluate_dates_holidays(df=df)
df = tsh.evaluate_dates_timeshifts(df=df)
df = mop.evaluate_dates_moonphases(df=df)
df = sst.evaluate_dates_seasonstarts(df=df)

## create lists of dates from calendar dataframe
l_holidays_calendar = []
l_timeShift_calendar = []
l_moonPhases_calendar = []
l_beginningOfSeason_calendar = []
for idx, row in df.iterrows():
    if not pd.isna(row["s_holiday"]):
        l_holidays_calendar.append(row["date_"].date())
    if not pd.isna(row["s_timeShift"]):
        l_timeShift_calendar.append(row["date_"].date())
    if not pd.isna(row["s_moonphase"]) and (row["i_year"] in [2025, 2026]):
        l_moonPhases_calendar.append(row["date_"].date())
    if not pd.isna(row["s_beginning_of_season"]):
        l_beginningOfSeason_calendar.append(row["date_"].date())
l_holidays_calendar = sorted(l_holidays_calendar)
l_timeShift_calendar = sorted(l_timeShift_calendar)
l_moonPhases_calendar = sorted(l_moonPhases_calendar)
l_beginningOfSeason_calendar = sorted(l_beginningOfSeason_calendar)


##### DEFINE DATE TO BE VERIFIED ##############################################################################

### HOLIDAY --------------------------------------------------------------------------------------------
d_holidays_to_verify = { ## verification dates from
    ## https://de.wikipedia.org/wiki/Karneval,_Fastnacht_und_Fasching
    ## https://de.wikipedia.org/wiki/Osterdatum
    ## https://de.wikipedia.org/wiki/Pfingsten
    ## https://de.wikipedia.org/wiki/Christi_Himmelfahrt
    "New Year's Day":     ["2025-01-01", "2026-01-01", "2027-01-01", "2028-01-01", "2029-01-01"],
    "St Berchtold's Day": ["2025-01-02", "2026-01-02", "2027-01-02", "2028-01-02", "2029-01-02"],
    "Good Tuesday":       ["2025-03-04", "2026-02-17", "2027-02-09", "2028-02-29", "2029-02-13"],
    "Ash Wednesday":      ["2025-03-05", "2026-02-18", "2027-02-10", "2028-03-01", "2029-02-14"],
    "Good Friday":        ["2025-04-18", "2026-04-03", "2027-03-26", "2028-04-14", "2029-03-30"],
    "Easter":             ["2025-04-20", "2026-04-05", "2027-03-28", "2028-04-16", "2029-04-01"],
    "Easter Monday":      ["2025-04-21", "2026-04-06", "2027-03-29", "2028-04-17", "2029-04-02"],
    "Ascension Day":      ["2025-05-29", "2026-05-14", "2027-05-06", "2028-05-25", "2029-05-10"],
    "Pentacost":          ["2025-06-08", "2026-05-24", "2027-05-16", "2028-06-04", "2029-05-20"],
    "Whit Monday":        ["2025-06-09", "2026-05-25", "2027-05-17", "2028-06-05", "2029-05-21"],
    "National Holiday":   ["2025-08-01", "2026-08-01", "2027-08-01", "2028-08-01", "2029-08-01"],
    "All Saints Day":     ["2025-11-01", "2026-11-01", "2027-11-01", "2028-11-01", "2029-11-01"],
    "Christmas Eve":      ["2025-12-24", "2026-12-24", "2027-12-24", "2028-12-24", "2029-12-24"],
    "Christmas Day":      ["2025-12-25", "2026-12-25", "2027-12-25", "2028-12-25", "2029-12-25"],
    "Boxing Day":         ["2025-12-26", "2026-12-26", "2027-12-26", "2028-12-26", "2029-12-26"],
    "New Year's Eve":     ["2025-12-31", "2026-12-31", "2027-12-31", "2028-12-31", "2029-12-31"],
}
l_holidays_to_verify = []
for k, v in d_holidays_to_verify.items():
    l_holidays_to_verify.extend(v)
l_holidays_to_verify = [datetime.strptime(x, "%Y-%m-%d").date() for x in l_holidays_to_verify]
l_holidays_to_verify = sorted(l_holidays_to_verify)


### MOON PHASES ----------------------------------------------------------------------------------------
d_moonPhases_to_verify = { ## verification dates from https://de.wikipedia.org/wiki/Mondphasen_(Tabelle)
    "new moon":  ["2025-01-29", "2025-02-28", "2025-03-29", "2025-04-27",
                  "2025-05-27", "2025-06-25", "2025-07-24", "2025-08-23",
                  "2025-09-21", "2025-10-21", "2025-11-20", "2025-12-20",
                  "2026-01-18", "2026-02-17", "2026-03-19", "2026-04-17",
                  "2026-05-16", "2026-06-15", "2026-07-14", "2026-08-12",
                  "2026-09-11", "2026-10-10", "2026-11-09", "2026-12-09"],
    "full moon": ["2025-01-13", "2025-02-12", "2025-03-14", "2025-04-13",
                  "2025-05-12", "2025-06-11", "2025-07-10", "2025-08-09",
                  "2025-09-07", "2025-10-07", "2025-11-05", "2025-12-05",
                  "2026-01-03", "2026-02-01", "2026-03-03", "2026-04-02",
                  "2026-05-01", "2026-05-31", "2026-06-30", "2026-07-29",
                  "2026-08-28", "2026-09-26", "2026-10-26", "2026-11-24",
                  "2026-12-24"],
}
l_moonPhases_to_verify = []
for k, v in d_moonPhases_to_verify.items():
    l_moonPhases_to_verify.extend(v)
l_moonPhases_to_verify = [datetime.strptime(x, "%Y-%m-%d").date() for x in l_moonPhases_to_verify]
l_moonPhases_to_verify = sorted(l_moonPhases_to_verify)


### BEGINNING OF SEASON --------------------------------------------------------------------------------
d_seasonStarts_to_verify = { ## verification dates from https://en.wikipedia.org/wiki/Season
    "begin_of_spring_astronomical":   ["2025-03-20", "2026-03-20", "2027-03-20", "2028-03-20", "2029-03-20"],
    "begin_of_summer_astronomical":   ["2025-06-21", "2026-06-21", "2027-06-21", "2028-06-20", "2029-06-21"],
    "begin_of_autumn_astronomical":   ["2025-09-22", "2026-09-23", "2027-09-23", "2028-09-22", "2029-09-22"],
    "begin_of_winter_astronomical":   ["2025-12-21", "2026-12-21", "2027-12-22", "2028-12-21", "2029-12-21"],
    "begin_of_spring_meteorological": ["2025-03-01", "2026-03-01", "2027-03-01", "2028-03-01", "2029-03-01"],
    "begin_of_summer_meteorological": ["2025-06-01", "2026-06-01", "2027-06-01", "2028-06-01", "2029-06-01"],
    "begin_of_autumn_meteorological": ["2025-09-01", "2026-09-01", "2027-09-01", "2028-09-01", "2029-09-01"],
    "begin_of_winter_meteorological": ["2025-12-01", "2026-12-01", "2027-12-01", "2028-12-01", "2029-12-01"]
}
l_seasonStarts_to_verify = []
for k, v in d_seasonStarts_to_verify.items():
    l_seasonStarts_to_verify.extend(v)
l_seasonStarts_to_verify = [datetime.strptime(x, "%Y-%m-%d").date() for x in l_seasonStarts_to_verify]
l_seasonStarts_to_verify = sorted(l_seasonStarts_to_verify)


### TIME SHIFT -----------------------------------------------------------------------------------------
d_timeShifts_to_verify = { ## verification dates from https://de.wikipedia.org/wiki/Sommerzeit
    "summer_time": ["2025-03-30", "2026-03-29", "2027-03-28", "2028-03-26", "2029-03-25"],
    "winter_time": ["2025-10-26", "2026-10-25", "2027-10-31", "2028-10-29", "2029-10-28"]
}
l_timeShifts_to_verify = []
for k, v in d_timeShifts_to_verify.items():
    l_timeShifts_to_verify.extend(v)
l_timeShifts_to_verify = [datetime.strptime(x, "%Y-%m-%d").date() for x in l_timeShifts_to_verify]
l_timeShifts_to_verify = sorted(l_timeShifts_to_verify)



##### DEFINE TEST CASES #######################################################################################

def test_holiday_dates():
    print("WEB:", l_holidays_to_verify)
    print("CAL:", l_holidays_calendar)
    assert (set(l_holidays_to_verify) == set(l_holidays_calendar))


def test_moonphase_dates():
    print("WEB:", l_moonPhases_to_verify)
    print("CAL:", l_moonPhases_calendar)
    for i, elem in enumerate(l_moonPhases_to_verify):
        moon_date_low = elem - timedelta(days=1)
        moon_date_high = elem + timedelta(days=1)
        print(i, elem, moon_date_low, moon_date_high, l_moonPhases_calendar[i])
        assert (moon_date_low <= l_moonPhases_calendar[i]) and (moon_date_high >= l_moonPhases_calendar[i])
    # assert (set(l_moonPhases_to_verify) == set(l_moonPhases_calendar))


def test_beginning_of_season_dates():
    print("WEB:", l_seasonStarts_to_verify)
    print("CAL:", l_beginningOfSeason_calendar)
    assert (set(l_seasonStarts_to_verify) == set(l_beginningOfSeason_calendar))


def test_timeshift_dates():
    print("WEB:", l_timeShifts_to_verify)
    print("CAL:", l_timeShift_calendar)
    assert (set(l_timeShifts_to_verify) == set(l_timeShift_calendar))
