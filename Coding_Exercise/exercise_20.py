# Loyalty Points Tracker

# You are building a Loyalty Points Tracker for a retail chain that rewards customers based on their
# spending. The tracker calculates the total transaction amount per customer and awards loyalty
# points accordingly. Some customers may also qualify for bonus points based on their total
# spending. 
# Tasks: 
# 1. Define a global variable loyalty_points that keeps track of the total loyalty
# points earned by all customers.
# 2. Create a function process_transactions(transactions: list[int]) -> int that:
# - Accepts a list of transaction amounts from a single customer.
# - Initializes a local variable total to store the sum of all the customer’s transactions.
# - Defines a nested function apply_bonus() that adds a ■50 bonus if total exceeds ■1000, using
# nonlocal.
# - Updates the global loyalty_points (1 point for every ■100 spent).
# - Returns the final total (including bonus if applicable). Example:
# process_transactions([400, 700])
# - total = 1100 → bonus applied → total = 1150
# - points earned = 11

loyalty_points = 0

def process_transactions(transactions: list[int] = None) -> int:
    if transactions is None:
        transactions = []
    total = sum(transactions)
    def apply_bonus():
        nonlocal total
        if total > 1000:
            total += 50
    apply_bonus()
    global loyalty_points
    points = total // 100
    loyalty_points += points
    return total
process_transactions()