daily_sales = [5, 10, 15, 20, 25, 30, 6, 11, 16, 21, 26, 31]

total_cups = sum( sale for sale in daily_sales if sale > 5)

print(total_cups)