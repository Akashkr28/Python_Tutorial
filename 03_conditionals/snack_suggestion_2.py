# A local cafe wants a program that suggests a snack. If a consumer asks for cookies
# samosa, it confirms the order. Otherwise, it says it's not available.

# Task:
#   - Take Snack Input
#   - If it's "cookies" or "samosa" , confirm the order
#   - Else, show unavailability


snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")