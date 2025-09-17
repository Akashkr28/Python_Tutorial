def brew_chai(flavor):
    if flavor not in["masala", "ginger", "elaichi"]:
        raise ValueError("chai is not available")
    print(f"{flavor} chai is brewing!")

brew_chai("mint")