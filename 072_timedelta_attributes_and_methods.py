from datetime import timedelta

# Create a timedelta object
example = timedelta(weeks=2, days=5, hours=7, minutes=20, seconds=45, microseconds=2500)

# Access timedelta attributes
print("Days:", example.days)
print("Seconds:", example.seconds)
print("Microseconds:", example.microseconds)

# Calculate total seconds
print("Total seconds:", example.total_seconds())
