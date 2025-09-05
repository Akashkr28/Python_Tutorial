def make_chai():
    # return "Here is your chai!"
    print("Here is your chai!")

return_value = make_chai()

# print(return_value)  # Output: Here is your chai!

def sold_cups():
    return 120

total = sold_cups()
print(total) # Output: 120


def chai_status(cups_left):
    if cups_left == 0:
        return "We are out of chai!"
    return "We have chai available."

print(chai_status(0))  # Output: We are out of chai!
print(chai_status(5))  # Output: We have chai available.

def chai_report():
    return 100, 20 # total cups, cups sold

sold, remaining = chai_report()
print("Sold : ", sold)
print("Remaining : ", remaining)