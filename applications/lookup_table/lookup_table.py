# Your code here
import math
import random

cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # First, we create a variable for the cache key and point it to a tuple of the values being passed in
    # This allows us to make a key using a combination of values
    key = (x, y)

    # Then we write a conditional to check if the values being passed in have already been calculated and stored in cache
    if key not in cache:
        # If the key is not cached already, we calculate the result and store it in cache
        cache[key] = slowfun_too_slow(x, y)
    
    # Lastly, after the result has been cached, we return the correct value for the values passed in
    return cache[key]

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
