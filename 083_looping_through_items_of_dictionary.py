countries = {
    "IN": "India",
    "CA": "Canada",
    "US": "United States",
    "MX": "Mexico",
    "DE": "Germany",
    "UK": "United Kingdom",
    "AU": "Australia",
    "NZ": "New Zealand",
}

# Loop through dictionary items and print key-value pairs
for key, value in countries.items():
    print(f"{key}: {value}", end="\t")

print()  # Add a newline for better readability

# Loop through dictionary items and print as tuples
for item in countries.items():
    print(item, end=" ")