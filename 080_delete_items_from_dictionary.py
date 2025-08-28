# Define a dictionary with country codes as keys and country names as values
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

# Remove the entry with the key "NZ" using the `del` statement
del countries["NZ"]

# Print the updated dictionary after deletion
print(countries)  # {'IN': 'India', 'CA': 'Canada', 'US': 'United States', 'MX': 'Mexico', 'DE': 'Germany', 'UK': 'United Kingdom', 'AU': 'Australia'}

# Remove the entry with the key "UK" using the `pop` method
removed_country = countries.pop("UK")

# Print the removed value and the updated dictionary
print(removed_country)  # 'United Kingdom'
print(countries)  # {'IN': 'India', 'CA': 'Canada', 'US': 'United States', 'MX': 'Mexico', 'DE': 'Germany', 'AU': 'Australia'}

# Clear all entries from the dictionary using the `clear` method
countries.clear()

# Print the dictionary after clearing all entries
print(countries)  # {}