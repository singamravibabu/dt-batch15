email = "vivek.kumar@gmail.com"

# Find the index of '@' in the email
at_index = email.find("@")
print("Index of '@':", at_index)

# Find the index of '.' after the '@'
dot_index = email.find(".", at_index + 1)
print("Index of '.':", dot_index)

# Check if '-' exists in the email
dash_index = email.find("-")
print("Index of '-':", dash_index)

# Validate the email address
if at_index == -1 or dot_index == -1:
    print("Invalid email address:", email)
else:
    print("Valid email address:", email)