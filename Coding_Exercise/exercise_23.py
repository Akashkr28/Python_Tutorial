# Smart Inventory Filter
# You are building a Smart Inventory Filter for a retail store.
# Tasks:

# 1. Process a list of product dictionaries, where each product has name, price, and category.
# 2. Use different types of comprehensions to:
#   - Extract names of products priced below ₹500 using list comprehension.
#   - Extract all unique categories using set comprehension.
#   - Create a name-to-price mapping using dictionary comprehension.
#   - Generate a list of discounted prices using a generator expression and convert it to a list.
# 3. Return all four outputs as a tuple.

products = [
    {"name": "Product A", "price": 1000, "category": "Electronics"},
    {"name": "Product B", "price": 500, "category": "Clothing"},
    {"name": "Product C", "price": 800, "category": "Electronics"},
    {"name": "Product D", "price": 1200, "category": "Clothing"},
    {"name": "Product E", "price": 600, "category": "Clothing"},
]


def smart_inventory_filter(products):
    names_below_500 = [product["name"] for product in products if product["price"] < 500]

    unique_categories = {product["category"] for product in products}

    name_to_price = {product["name"]: product["price"] for product in products}

    discounted_prices = (price * 0.9 for price in name_to_price.values())
    
    return names_below_500, unique_categories, name_to_price, list(discounted_prices)

names_below_500, unique_categories, name_to_price, discounted_prices = smart_inventory_filter(
    products
)

print("Names of products priced below ₹500:", names_below_500)
print("Unique categories:", unique_categories)
print("Name-to-Price Mapping:", name_to_price)
print("Discounted Prices:", discounted_prices)