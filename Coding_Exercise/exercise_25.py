# Caching Expensive Calculations
# You are optimizing performance for a system that frequently repeats the same heavy calculations (e.g., a backend system or a financial calculator).

# Tasks:

# 1. Create a decorator called cache_results:
#   - Use a dictionary to store past results based on arguments.
#   - If the same arguments are passed again, return the cached result.
#   - Otherwise, compute the result, cache it, and return the new value.

# 2. Apply it to a function multiply(a, b):
#   - It simply returns the product of two integers.

# 3. The decorated function should:
#   - Return "Computed: result" for new computations.
#   - Return "From Cache: result" for repeated calls with the same arguments.

from functools import wraps

def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in cache:
            return f"From Cache: {cache[key]}"
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return f"Computed: {result}"
        
    return wrapper

@cache_results
def multiply(a, b):
    return a * b
# Example usage:
print(multiply(3, 4))  # Computed: 12
print(multiply(3, 4))  # Computed: 12