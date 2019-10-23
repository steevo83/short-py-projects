from collections import defaultdict as ddict

def mod(n, mod):
    return n%mod

def mult(n, mod):
    return n*mod

def group_by(numbers, key_func=lambda n, mod: n, mod_num=0):
    dd = ddict(list)
    for num in numbers:
        dd[key_func(num, mod_num)].append(num)
    return dd
    

group_by([1,1,1,70,2,3,70, 80, 90, 4, 5, 6, 7], key_func=None, mod_num=4)


# This week I want you to make a function that takes an iterable and a key 
# function and returns a dictionary of items grouped by the values returned by 
# the given key function.

# For example, let's say we have a list of numbers, and a function that checks 
# their remainder when we divide them by three.

# >>> numbers = [1, 4, 5, 6, 8, 19, 34, 55]
# >>> def mod3(n): return n % 3
# ...

# If we call our function with this list and key function, we should get the 
# numbers back in a dictionary of numbers tied to their remainders (0, 1, 2).

# >>> group_by(numbers, key_func=mod3)
# {0: [6], 1: [1, 4, 19, 34, 55], 2: [5, 8]}

# As a bonus, create a default behavior of returning the value back in the 
# case that no key function is given. ✔️

# >>> group_by([1, 2, 1, 3, 2, 1])
# {1: [1, 1, 1], 2: [2, 2], 3: [3]}