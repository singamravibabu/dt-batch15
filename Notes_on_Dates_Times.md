# WORKING WITH DATES AND TIMES

- The `datetime` module contains constructors for constructing dates and times.
- To use constructors, we pass arguments to them in the same way we pass arguments to methods.
- From `datetime` we use `date` constructor to construct date objects, `time` constructor to construct time objects, and `datetime` constructor to construct datetime objects.
```
from datetime import date, time, datetime
```
- Methods of date and datetime classes:
    1. date.today() 
        Returns a date object for the current date.
    2. datetime.now()
        Returns a datetime object for the current date and time.

- The constructors for creating date, time and datetime objects:
    1. date(year, month, day)
    2. time(hour, minute, second, microsecond)
    3. datetime(year, month, day[, hour][, minute][, second][, microsecond])

##### Create datetime objects by parsing string
- The `datetime.strptime()`:
    - The p in the strptime() method stands for parse.
    - We can use this method to create a datetime object from a string.
- To specify the format of the string we format codes.
- Syntax:
```
strptime(date_string, format_str)
```
- Command format string codes:
    %d  Day of month as a number
    %m  Month as a number
    %Y  Year with century as a decimal number
    %y  Year without century as a decimal number
    %H  Hour (24-hour clock) as a decimal number
    %I  Hour (12-hour clock) as a decimal number
    %M  Minute as a decimal number
    %S  Second as a decimal number
    %f  Microsecond