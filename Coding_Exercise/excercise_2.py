"""
Should You Go for a Walk ?

You’re deciding whether to go for a walk based on two real-life conditions:

    is_sunny = True
    have_umbrella = False

Print the result of the following:
    1. Is it not sunny today?
    2. Do you not have an umbrella?
    3. Should you go for a walk if it’s sunny and you don’t need an umbrella?
    4. Should you go for a walk if it’s sunny or if you have an umbrella?
"""

is_sunny = True
have_umbrella = False

print(not is_sunny)
print(not have_umbrella)
print((is_sunny) and (not have_umbrella))
print((is_sunny) or (not have_umbrella))