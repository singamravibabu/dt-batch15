from decimal import Decimal

# Importing the Decimal class from the decimal module for precise decimal arithmetic

# Performing arithmetic with Decimal objects to maintain precision
print(Decimal('100.1') + Decimal('100.1') + Decimal('100.1'))  # Expected: 300.3
print(Decimal('300.3'))  # Expected: 300.3

# Demonstrating the difference between float and Decimal arithmetic
x = 100.1  # Float value
print(x + x + x)  # May result in a precision error due to floating-point arithmetic

y = Decimal('100.1')  # Decimal value
print(y + y + y)  # Precise result with Decimal arithmetic

# Printing the Decimal object
print(y)  # Expected: 100.1

# Repeating the Decimal addition for clarity
print(y + y + y)  # Expected: 300.3

# Printing the float and Decimal values for comparison
print(x)  # Float value: 100.1
print(y)  # Decimal value: 100.1

# Adding float and integer
print(x + 100)  # Float addition: 200.1
# Adding Decimal and integer
print(y + 100)  # Decimal addition: 200.1

# Mixing float and Decimal in arithmetic (not recommended due to type differences)
print(Decimal(x) + y)  # Convert float to Decimal for consistent precision