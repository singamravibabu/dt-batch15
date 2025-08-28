countries = {
    "IN": "India",
    "CA": "Canada",
    "US": "United States",
    "MX": "Mexico",
    "DE": "Germany"
}

# Accessing existing keys
print(countries["IN"])  # Output: India
print(countries["MX"])  # Output: Mexico
print(countries["DE"])  # Output: Germany

# Using a non-existent key throws a KeyError
print(countries["JP"])  # Output: Key not found
