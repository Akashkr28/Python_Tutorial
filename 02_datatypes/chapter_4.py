is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling #upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk
print(f"Milk present: {bool(milk_present)}")

# Conditional Operators

water_hot = True
tea_added = True

con_serve = water_hot and tea_added
print(f"Condition to serve tea: {con_serve}")