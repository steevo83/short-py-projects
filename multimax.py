def multimax(vals, key=lambda x:x):
    max_key=None
    maxes=[]        
    for item in vals:
        k = key(item)
        if k == max_key:
            maxes.append(item)
        elif not maxes or k > max_key:
            maxes = [item]
            max_key = k
    return maxes
    # return [nums for nums in values if nums == max(values, key=key)]

# key=len
# print(key("ministry"))
# print(len("ministry"))
# print("ministry")

# def multimax(vals, key=lambda x:x):
#     values = list(vals)
#     compare = {}
#     for item in values:
#         compare[item] = key(item)
#     #maxes = [compare[maximum] for maximum in compare.values if max(compare)]
#     #print(values)
#     maxvalue = max(values, key=key)
#     print(maxvalue)
#     #maxes = {item: value for item, key(item) in values}
#     #return maxes
    
numbers = [1, 3, 8, 5, 4, 10, 6]
# #print(numbers)
# odds = (n for n in numbers if n % 2 == 1)
# #print(odds)

# #print(list(odds))
words = ["cheese", "shop", "ministry", "of", "silly", "walks", "walks", "argument", "clinic"]
multimax(words)
multimax(numbers, key=lambda x: x%2)




#print([item for item in words if max(words, key=len)])

# print(max(["test", "long word", "sh"], key=lambda x:x))
# print(max(["test", "long word", "sh"], key=len))

# This week I want you to write a function that takes an iterable and returns all maximum values found in the given iterable.

# By "all maximum values" I mean that if there are multiple values in a list that are all seen as maximums, then a list of all the values should be returned. If there is just one maximum value, then a list with the single value should be returned.

# For example:

# >>> multimax([1, 2, 4, 3])
# [4]
# >>> multimax([1, 4, 2, 4, 3])
# [4, 4]
# >>> multimax((1, 1, 1))
# [1, 1, 1]

# For the first bonus, I want you to make sure your multimax function returns an empty list if the given iterable is empty: ✔️

# >>> multimax([])
# []

# For the second bonus, I want you to make sure your multimax function will work with iterators (lazy iterables) such as files, zip objects, and generators ✔️:

# >>> numbers = [1, 3, 8, 5, 4, 10, 6]
# >>> odds = (n for n in numbers if n % 2 == 1)
# >>> multimax(odds)
# [5]

# For the third bonus, I want you to make your multimax function accept a 
# keyword argument called "key" that is a function which will be used to 
# determine the key by which to compare values as maximums. For example the 
# key function could be used to find the longest words in a list of words ✔️:

# >>> words = ["cheese", "shop", "ministry", "of", "silly", "walks", "argument", "clinic"]
# >>> multimax(words, key=len)
# ['ministry', 'argument']

