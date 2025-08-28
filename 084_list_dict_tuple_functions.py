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

# Convert dictionary keys to a list
codes_list = list(countries.keys())
print(codes_list)  # Output: ['IN', 'CA', 'US', 'MX', 'DE', 'UK', 'AU', 'NZ']

# Convert dictionary values to a tuple
country_tuple = tuple(countries.values())
print(country_tuple)  # Output: ('India', 'Canada', 'United States', 'Mexico', 'Germany', 'United Kingdom', 'Australia', 'New Zealand')

# Convert dictionary items to a list of tuples
items_list = list(countries.items())
print(items_list)  # Output: [('IN', 'India'), ('CA', 'Canada'), ('US', 'United States'), ('MX', 'Mexico'), ('DE', 'Germany'), ('UK', 'United Kingdom'), ('AU', 'Australia'), ('NZ', 'New Zealand')]

# Convert a list of lists to a dictionary
numbers = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]]
numbers_dict = dict(numbers)
print(numbers_dict)  # Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
