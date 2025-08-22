# Splitting a quotation into words
quotation = "These are the times that try men's souls."
words = quotation.split()
print(words)  # ['These', 'are', 'the', 'times', 'that', 'try', "men's", 'souls.']
print(words[0])  # 'These'
print(words[-1])  # 'souls.'

# Splitting a date string into components
date = "9/25/2015"
date_parts = date.split('/')
print(date_parts)  # ['9', '25', '2015']

# Converting date components to integers
month, day, year = map(int, date_parts)
print(month)  # 9
print(day)    # 25
print(year)   # 2015

# Splitting an address string into components
address = "Raj Kumar|18-29|Gautamnagar|Malkajgiri|Hyderabad|500047"
address_parts = address.split("|")
print(address_parts)  
# ['Raj Kumar', '18-29', 'Gautamnagar', 'Malkajgiri', 'Hyderabad', '500047']
