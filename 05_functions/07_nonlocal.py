def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Adrak"
    kitchen()
    print("After kitcher update", chai_type)
update_order()