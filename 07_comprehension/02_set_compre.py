favourite_chai = [
    "Masala Chai", "Green Tea", "Masala Chai",    
    "Lemaon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chai}
print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardmom", "clove"],
    "Elaichi Chai": ["cardmon", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredient in recipes.values() for spice in ingredient}

print(unique_spices)