# When solving this week's exercise, make sure to hold off on searching directly for the answer in Google/StackOverflow. 🚫🔍 This is a fairly general exercise and there are a number of answers to it. I'd like you to struggle to come to an answer or two (or five?) on your own.

# I want you to write a function that accepts a string and returns a mapping (a dictionary or dictionary-like structure) that has words as the keys and the number of times each word was seen as the values.

# Your function should work like this:

# >>> count_words("oh what a day what a lovely day")
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
# >>> count_words("don't stop believing")
# {"don't": 1, 'stop': 1, 'believing': 1}

# As a bonus, make sure your function works well with mixed case words:

# >>> count_words("Oh what a day what a lovely day")
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}

# For even more of a bonus try to get your function to ignore punctuation outside of words:

# >>> count_words("Oh what a day, what a lovely day!")
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
from collections import defaultdict as dd
import string
import re

def count_words(text):
    final = dd(int)
    strip_punc = re.sub(r"[^\w\d'\s]","",text).split()
    #strip_punc = text.translate(str.maketrans(dict.fromkeys(string.punctuation))).split()
    for each in strip_punc:
        final[each.lower()] += 1
    return dict(final)


print(count_words("¿all cool lower some Upper case'd letters and all cool!"))

