from datetime import datetime

# Parse different date formats
dt1 = "2025-08-28"
dt2 = "8/24/2025"
dt3 = "8/18, 2025"
dt4 = "23rd of 8th month, this year - 2025, at 10 hours, 45 minutes"

dt1 = datetime.strptime(dt1, "%Y-%m-%d")
print(dt1)  # Output: 2025-08-28 00:00:00

dt2 = datetime.strptime(dt2, "%m/%d/%Y")
print(dt2)  # Output: 2025-08-24 00:00:00

dt3 = datetime.strptime(dt3, "%m/%d, %Y")
print(dt3)  # Output: 2025-08-18 00:00:00

dt4 = datetime.strptime(dt4, "%drd of %mth month, this year - %Y, at %H hours, %M minutes")
print(dt4)  # Output: 2025-08-23 10:45:00
