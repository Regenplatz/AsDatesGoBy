# As Dates Go By

<a href=https://www.python.org/>
    <img src=https://img.shields.io/badge/Python-grey?logo=python&logoColor=FFE05D alt="Python">
</a>

<a href=https://pandas.pydata.org/>
    <img src=https://img.shields.io/badge/Pandas-grey?logo=pandas&logoColor=130654 alt="Pandas">
</a>

<a href=https://pymeeus.readthedocs.io/en/latest/>
    <img src=https://img.shields.io/badge/PyMeeus-grey alt="PyMeeus">
</a>

<a href=https://en.wikipedia.org/wiki/Central_European_Time>
    <img src=https://img.shields.io/badge/timezone-CET-blue alt="Time Zone: CET">
</a>


<br>

<a id="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About the package</a></li>   
    <li><a href="#calendar">Calendar</a></li> 
    <li><a href="#holidays">Holidays</a></li>
    <li><a href="#time-shifts">Time Shifts</a></li>
    <li><a href="#moon-phases">Moon Phases</a></li>    
    <li><a href="#beginnings-of-seasons">Beginnings of Seasons</a></li>
  </ol>
</details>

<br>


## About this project
Goal of this project was to create a calendar dataframe, that contains date-specific information
as well as info on date-specific events (holidays, time shifts, moon phases, season starts).

Therefore, a calendar dataframe is created in first place. Then, further columns on event-specific
information are added.

The calendar dataframe containing all information is created by calling [main.py](main.py).
This file calls all files in the [src](src) folder in the provided order.
The final calendar contains following columns:

| column                | data type | created by file                                                  | example             |
|-----------------------|-----------|------------------------------------------------------------------|---------------------|
| i_year                | int       | [createCalendar.py](src/createCalendar.py)                       | 2025                |
| i_month               | int       | [createCalendar.py](src/createCalendar.py)                       | 1                   |
| s_month_short         | str       | [createCalendar.py](src/createCalendar.py)                       | Jan                 |
| s_month_long          | str       | [createCalendar.py](src/createCalendar.py)                       | January             |
| i_week                | int       | [createCalendar.py](src/createCalendar.py)                       | 1                   |
| i_dayofmonth          | int       | [createCalendar.py](src/createCalendar.py)                       | 1                   |
| i_weekday_iso         | int       | [createCalendar.py](src/createCalendar.py)                       | 1                   |
| s_weekday_short       | str       | [createCalendar.py](src/createCalendar.py)                       | Mon                 |
| s_weekday_long        | str       | [createCalendar.py](src/createCalendar.py)                       | Monday              |
| b_weekend             | int       | [createCalendar.py](src/createCalendar.py)                       | 1                   |
| s_holiday             | str       | [evaluateDates_holidays.py](src/evaluateDates_holidays)          | New Year            |
| b_workingday          | int       | [createCalendar.py](src/createCalendar.py)                       | 1                   |
| s_timeshift           | str       | [evaluateDates_timeShifts.py](src/evaluateDates_timeShifts.py)   | begin summer time   |
| s_moonphase           | str       | [evaluateDates_moonPhases.py](src/evaluateDates_moonPhases.py)   | full moon           |
| s_beginning_of_season | str       | [evaluateDates_seasonStarts.py](src/evaluateDates_seasonStarts.py) | beginning of summer |

Note: *b_weekend* and *b_workingday* are encoded as integers (0, 1), but could also be of type bool.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Calendar
The basic calendar dataframe contains columns on:
- year (int)
- month (int, str (short, e.g. "Jan"), str (long, e.g. "January"))
- week (int)
- day of month (int)
- iso-weekday (int, str (short, e.g. "Mon"), str (long, e.g. "Monday"))
- weekend (bool)

It is expanded by further columns for date-specific events.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Holidays
`Fixed Holidays` (such as *New Year* and *Christmas*) take place each year at the same day of month
and month. Therefore, they can easily be evaluated. 

For `Floating Holidays` (such as *Ash Wednesday* or *Good Friday*) the **Easter** dates for the 
given years are calculated as basis. From these, floating holidays could be calculated as relative 
differences to the evaluated *Easter* date of the year of interest.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Time Shifts
Time shifts take place each year on:
- the last Sunday in March (to change to summer time)
- the last Sunday in October (to change to winter time)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Moon Phases
To evaluate the [lunar phases](https://en.wikipedia.org/wiki/Lunar_phase), the approximation of 
29.53058 days (days=29, hours=12, minutes=44, seconds=3) as mean *synodic month* is used.

To calculate all following `Full Moons` and `New Moons` [lunation 0](https://en.wikipedia.org/wiki/New_moon)
was used as reference start date. <br>
This date describes the first new moon of 2000 at approximately 
18:14 UTC, 6 January 2000.

Note: In this project, moon phases were calculated based on *Central European Time* and might potentially
slightly differ from calendars that refer to calculated moon phases in UTC-format.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Beginnings of Seasons
`Meteorological Beginnings of Seasons` are calculated for each year as they occur every year on:
- March 1st (beginning of spring)
- June 1st (beginning of summer)
- September 1st (beginning of autumn)
- December 1st (beginning of winter)

To calculate `Astronomical Beginnings of Seasons`, various astronomical factors need to be taken into account. <br>
In this project, the package [PyMeeus](https://pymeeus.readthedocs.io/en/latest/) is used for simple calculation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
