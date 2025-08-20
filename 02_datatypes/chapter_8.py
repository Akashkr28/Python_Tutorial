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

# Overloading

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"full liquid mix: {full_liquid_mix}")

strong_brew = ["black tea"] * 3
print(f"strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINAMON")
raw_spice_data = raw_spice_data.replace(b"CINA", b"CARD")
print(f"Bytes: {raw_spice_data}")