essential_spices = {"cardamom", "ginger", "cinanamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"Spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"only in essentials: {only_in_essential}")

print(f"is 'cloves' in essential spices? {'cloves' in essential_spices}")
print(f"is 'cloves' in optional spices? {'cloves' in optional_spices}")

my_list = [1, 2, 3, 2, 4]
frozen_set_1 = frozenset(my_list)
print(f"frozen_set_1")
