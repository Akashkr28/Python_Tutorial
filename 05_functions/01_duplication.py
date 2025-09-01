# Reducing Code Duplication
# You receive many order and want to print each customer's name along with the type of chai
# they ordered.
# Task:
#   - Write a function `print_order(name, chai_type)`
#   - Call it multiple times for different customers

def print_order(name, chai_type): # we define parameter here
    print(f"{name} ordered {chai_type} chai")


print_order("Akash", "masala") # we define argument here
print_order("Amit", "ginger")
print_order("Jia", "Tulsi")