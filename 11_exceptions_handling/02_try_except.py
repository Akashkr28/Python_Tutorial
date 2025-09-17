chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["mint"]
except KeyError:
    print("Sorry, mint chai is not available")

print("Program continues...")