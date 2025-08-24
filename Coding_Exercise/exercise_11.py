# Age Verification System

# You're building a system to verify user age for access
# Task
#   - Define a function to verify_age that accepts a 'string' input named age_str
#   - Convert age_str to an integer using int(.
#   - Use a ternary operator to return:
#       - "Access Granted" if age is 18 or older
#       - "Access Denied" otherwise

verify_age = int(input("age_str: "))

age = print("Access Granted") if verify_age >= 18 else print("Access Denied")

