# You're building a ticket info system for a railway app.
# Based on seat type, show it's features.

# Task:
#   - Input: `sleeper`, `AC`, `general`, `luxury`
#   - Match using `match-case`
#   - Unknown -> show: `Invalid Seat Type`


seat_type = input("Enter the seat type: (sleeper/AC/General/Luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, Beds available")
    case "ac":
        print("AC - Air Conditioned, comfy ride")
    case "general":
        print("General - Cheapest Option, No reservation")
    case "luxury":
        print("luxury - Premium seats with meals")
    case _:
        print("Invalid Seat Type")