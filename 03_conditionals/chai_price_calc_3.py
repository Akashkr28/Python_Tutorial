# A tea stall offers different prices for different cup sizes. Write a program that calulates price based on size.

# Task:
#   - Input "small", "medium", "large"
#   - Small -> Rs. 10, Medium -> Rs. 15, Large -> Rs. 20
#   - If invalid: show "Unknown Cup Size"

cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is Rs. 10")
elif cup == "mediium":
    print("Price is Rs. 15")
elif cup == "large":
    print("Price is Rs. 20")
else:
    print("Unknown cup size")