# Loan Eligibility Checker

# You’re building a basic loan eligibility checker for a bank. A customer must meet two conditions to be eligible:

# Task
#   - If the user’s age is 21 or above, check:
#       - If income is 25,000 Bucks or above, return: "Eligible for loan"
#       - Otherwise, return: "Not eligible for loan"
#   - If the user's age is less than 21, return "Not eligible: Age must be 21 or above"

age = int(input("Age: "))

if age >= 21:
    income = int(input("Income: "))
    if income >= 25000:
        print("Eligible for loan")
    else:
        print("Not eligible for loan")
else:
    print("Not eligible: Age must be 21 or above")