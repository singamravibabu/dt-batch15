message = "the meaning of life"

print(message.endswith("e"))       # True
print(message.endswith("life"))    # True
print(message.endswith("ife"))     # True
print(message.endswith("life."))   # False
print(message.endswith("."))       # False
print(message.endswith("!"))       # False
