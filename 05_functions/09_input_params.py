# chai = "Ginger chai"

# def prepare_chai(order):
#     print(f"Preparing your {order}...")

# prepare_chai(chai)
# print(chai)

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") # Positional arguments
make_chai(tea="Green", sugar="Medium", milk="No") # Keyword arguments

def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

special_chai("Cinamon", "Cardamom", sweetener="Honey", foam="Yes")


# def chai_order(order=[]):
#     order.append("masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()