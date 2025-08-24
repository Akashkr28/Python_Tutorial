# Food menu Selector

get_item_price  = input("item: ").lower()

match get_item_price:
    case "pizza":
        print("Rs. 10")
    case "burger":
        print("Rs. 15")
    case "pasta":
        print("Rs. 20")
    case _:
        print("Item not found")