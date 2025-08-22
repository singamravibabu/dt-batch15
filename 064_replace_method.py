# Replace dashes in credit card number with spaces
cc_number = "4401-881022-88810".replace("-", " ")
print(cc_number)  # Output: 4401 881022 88810

# Remove dashes from phone number
phone_number = "555-555-1234".replace("-", "")
print(phone_number)  # Output: 5555551234

# Format phone number as (XXX)XXX-XXXX
formatted_phone_number = f"({phone_number[:3]}){phone_number[3:6]}-{phone_number[6:]}"
print(formatted_phone_number)  # Output: (555)555-1234
