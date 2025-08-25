# Generate Multiplication Table
# You are developing a feature in an educational app that displays multiplication tables.

# Tasks:

#   - Write a function named multiplication_table that takes a single integer argument number.
#   - Using a for loop and range(), generate the multiplication table for number from 1 to 10.
#   -Return a list of strings in the following format:
#       -"number x i = result"
#       -(Example: "3 x 4 = 12")

multiplicatiob_table = int(input("number"))

for i in range(1, 11):
    result = multiplicatiob_table * i
    print(f"{multiplicatiob_table} x {i} = {result}")