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

##### Formatting Dates and Times
- The `strftime()` method:
    - The f in the strftime() method stands for format.
    - We can use this method to create a string from a datetime object.strftime(format_str)
- Command format string codes:
    %a  Abbreviated weekday name
    %A  Full weekday name
    %b  Abbreviated month name
    %B  Full month name
    %d  Day of month as a decimal number
    %m  Month as a decimal number
    %y  Year without century as a decimal number
    %Y  Year with century as a decimal number
    %w  Weekday as a decimal number
    %H  24-Hour as a decimal number
    %I  12-Hour as a decimal number
    %M  Minute as a decimal
    %S  Second as a decimal number
    %p  Locale equivalent of either AM or PM


## Working with Spans of Time
- A timedelta object stores a span of time.
- We can adjust a date or datetime object by adding or subtracting a timedelta object.
- We can also get the span of time between two date/time object by subtracting one from the other.
- Syntax for timedelta:
    timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

##### 3 attributes and one method of a timedelta object
1. days
    Returns the number of days
2. seconds
    Returns the number of seconds in addition to days
3. microseconds
    Returns the number of microseconds in addition to seconds and days
4. total_seconds()
    Returns total number of seconds and microseconds


#### Attributes that return the parts of date/time object
Readable attributes
year - Returns the year of the date/time object
month - Returns the month of the date/time object
day - Returns the day of the date/time object
hour - Returns the hour of the date/time object
minute - Returns the minute of the date/time object
second - Returns the second of the date/time object
microsecond - Returns the microsecond of the date/time object
