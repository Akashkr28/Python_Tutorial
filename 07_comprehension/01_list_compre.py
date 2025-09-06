menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea"
]

iced_tea = [ tea for tea in menu if "Iced" in tea ]
iced_tea = [ tea for tea in menu if len(tea) > 12 ]

print(iced_tea)