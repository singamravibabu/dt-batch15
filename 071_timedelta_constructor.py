from datetime import date, datetime, timedelta

# Define time durations
three_weeks = timedelta(weeks=3)
project_duration = timedelta(weeks=6, days=4)
meeting_span = timedelta(hours=3, minutes=45)

# Calculate the number of days until a specific date
num_of_days = date(2025, 10, 15) - date.today()

# Calculate a date after three weeks from today
after_three_weeks = date.today() + three_weeks

# Calculate a datetime after a specific duration
future_datetime = datetime.now() + timedelta(hours=3, minutes=15)

# Print results
print("Three weeks duration:", three_weeks)
print("Project duration:", project_duration)
print("Meeting span:", meeting_span)
print("Number of days until 2025-10-15:", num_of_days)
print("Date after three weeks:", after_three_weeks)
print("Future datetime:", future_datetime)
