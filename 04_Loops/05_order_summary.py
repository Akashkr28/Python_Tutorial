# You are preparing an order summary with customer names and their total bill.
# Task:
#   - Use two lists: one for names and one for bills.
#   - Print: "[Name] paid Rs. [Bill]"

names = ["Akash", "Sushant", "Rohit", "Rahul", "Ramesh"]
bills = [50, 70, 40, 60, 80]

for name, bill in zip(names, bills):
    print(f"{name} has to pay Rs. {bill}")