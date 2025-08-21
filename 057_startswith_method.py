message = "the meaning of life"

print(message.startswith("the"))    # True
print(message.startswith("t"))      # True
print(message.startswith("The"))    # False
print(message.startswith("there"))  # False
print(message.startswith("the m"))  # True
