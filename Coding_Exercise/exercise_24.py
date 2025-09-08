# Smart Token Dispenser
# You are developing a Smart Token Dispenser system, like those found in banks or clinics. This system reset counters based on user activity and needs to run until manually stopped.

# Tasks:
# 1. Create an infinite generator function called token_dispenser(start=1).
# 2. On each call to next(), it should yield the current token number and increment it.
# 3. If a value is passed to the generator using send(), the generator should reset the token number to that new value.
# 4. The generator should handle the .close() method gracefully and print "Dispenser closed." when it is closed.

"""
    Infinite generator that simulates a token dispenser.
    
    - Yields incrementing token numbers starting from `start`.
    - Accepts input via `send()` to optionally reset the counter to a new value.
    - Gracefully stops if `close()` is called.
"""

def token_dispenser(start: int = 1):
    # Yield the current token and wait for an optional 'send()' value
    token = start
    try:
        while True:
            new_start = yield token
            if new_start is not None:   # if send() provides a value
                token = new_start       # reset counter
            else:
                token += 1              # # otherwise increment normally
    except GeneratorExit:
        print("Dispenser Closed")

dispenser = token_dispenser(1)

print(next(dispenser))   # 1 (start)
print(next(dispenser))   # 2
print(next(dispenser))   # 3

# Reset token using send()
print(dispenser.send(100))  # Reset → yields 100
print(next(dispenser))      # 101
print(next(dispenser))      # 102

# Close gracefully
dispenser.close()