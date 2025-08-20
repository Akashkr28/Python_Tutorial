my_cart =  ["apples", "bananas", "milk"]
print(f"grocery_list = {my_cart}")

my_cart.append("bread")
print(f"grocery_list = {my_cart}")

my_cart.insert(0, "ketchup");
print(f"grocery_list = {my_cart}")

my_cart.remove("bananas")
print(f"grocery_list = {my_cart}")

removed_item = my_cart.pop()
print(f"grocery_list = {my_cart}")

update_list = ["rice", "butter"]
my_cart.extend(update_list)
print(f"grocery_list = {my_cart}")

my_cart.sort()
print(f"grocery_list = {my_cart}")

my_cart.reverse()
print(f"grocery_list = {my_cart}")

another_list = ["juice", "jam"]
my_new_cart = my_cart + another_list
print(f"new_cart = {my_new_cart}")

my_cart = my_cart * 2
print(f"grocery_list = {my_cart}")

vegetables = "tomato cucumber spinach"
veg_list = vegetables.split()
print(f"{veg_list}")