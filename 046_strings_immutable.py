# Strings in Python are immutable, meaning their content cannot be changed after creation.
# Attempting to modify a string directly will result in a TypeError.

# Define a string
message = "Hello out there!"

# The following line will raise an error because strings are immutable.
# Uncomment it to see the error: TypeError: 'str' object does not support item assignment
message[0] = 'W'

# To modify a string, you need to create a new string.
# For example, if you want to replace the first character:
message = 'W' + message[1:]  # Create a new string with the desired modification

# Print the modified string
print(message)  # Output: "Wello out there!"