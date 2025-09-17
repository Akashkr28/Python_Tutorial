class OutOfIngridientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngridientsError("Missing Milk or sugar")
    print("Chai is ready...")

make_chai(0, 2)