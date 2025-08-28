countries = {
    "IN": "India",
    "CA": "Canada",
    "US": "United States",
    "MX": "Mexico",
    "DE": "Germany"
}

# Accessing an existing key
print(countries["IN"])  # Output: 'India'

# Accessing a non-existing key using get() to avoid KeyError
print(countries.get("JP"))  # Output: None
print(countries.get("JP", "Unknown"))  # Output: 'Unknown'

# Accessing an existing key with a default value
print(countries.get("MX", "Unknown"))  # Output: 'Mexico'
