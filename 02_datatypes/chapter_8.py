ingredients = ["water", "milk", "black tea"]

ingredients.append("sugar")
print(f"ingredients: {ingredients}")

ingredients.remove("water")
print(f"ingredients: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai ingredients: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"chai ingredients: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"last added: {last_added}")

chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

chai_ingredients.sort()
print(f"chai ingredients: {chai_ingredients}")

sugar_levels = [5, 10, 15, 20, 25, 30]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")