# Dictionary in Python

chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"chai order: {chai_order}")

chai_recipe =  {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe liquid: {chai_recipe['liquid']}")

print(f"Recipe: {chai_recipe}")


del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")


print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "medium", "sugar": 1}
# print(f"order details (keys): {chai_order.keys()}")
# print(f"order details (values): {chai_order.values()}")
# print(f"order details (itens): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed Last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "chopped"}
chai_recipe.update(extra_spices)
print(f"Updated recipe: {chai_recipe}")

customer_note = chai_order.get("note", "NO Note")
print(f"Customer note: {customer_note}")