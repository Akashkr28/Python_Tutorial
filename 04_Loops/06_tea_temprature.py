# You want to simulate tea heating.
# It starts at 40 c and boils at 100 c
# Task
#   - Use a while Loop
#   - Increase temprature by 15 until it reaches or exceeds 100
#   - Print each temprature step

temp = 40

while temp < 100:
    # temp = temp + 15
    temp += 15
    print(f"Current temp: {temp}")

print("Tea is ready to boil") 