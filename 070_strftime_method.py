from datetime import datetime

def format_datetime_examples():
    """
    Demonstrates various datetime formatting options using strftime.
    """
    dt1 = datetime(2025, 8, 31)
    dt2 = datetime(2025, 9, 5, 9, 30) # This variable is defined but not used in the original snippet.
    dt3 = datetime(2025, 10, 15, 6, 30)

    print(f"dt1: {dt1}")
    print(f"dt1 formatted as '(%%a) %%B %%d, %%Y': {dt1.strftime('(%a) %B %d, %Y')}")
    print(f"dt1 formatted as '%%b %%d, 2025 (%%A)': {dt1.strftime('%b %d, 2025 (%A)')}")
    print(f"dt1 formatted as '%%Y - %%B %%d (%%a)': {dt1.strftime('%Y - %B %d (%a)')}")
    print(f"dt1 formatted as '%%Y - %%B %%d (%%w) - %%A': {dt1.strftime('%Y - %B %d (%w) - %A')}")

    dt3_evening = datetime(2025, 10, 15, 18, 30)
    print(f"\ndt3_evening: {dt3_evening}")
    print(f"dt3_evening formatted as '%%H:%%M @ %%A %%d, %%Y': {dt3_evening.strftime('%H:%M @ %A %d, %Y')}")
    print(f"dt3_evening formatted as '%%H:%%M @ %%B %%d, %%Y': {dt3_evening.strftime('%H:%M @ %B %d, %Y')}")
    print(f"dt3_evening formatted as '%%H:%%M %%p @ %%B %%d, %%Y': {dt3_evening.strftime('%H:%M %p @ %B %d, %Y')}")
    print(f"dt3_evening formatted as '%%I:%%M %%p @ %%B %%d, %%Y': {dt3_evening.strftime('%I:%M %p @ %B %d, %Y')}")
    print(f"dt3_evening formatted as '%%B %%d, %%Y @ %%I:%%M %%p': {dt3_evening.strftime('%B %d, %Y @ %I:%M %p')}")
    print(f"dt3_evening formatted as '%%B %%d, %%Y @ %%I:%%M %%p - (%%A)': {dt3_evening.strftime('%B %d, %Y @ %I:%M %p - (%A)')}")

if __name__ == "__main__":
    format_datetime_examples()
