# I want you to write a function that accepts two strings and returns True if the two strings are anagrams of each other.

# Your function should work like this:

# >>> is_anagram("tea", "eat")
# True
# >>> is_anagram("tea", "treat")
# False
# >>> is_anagram("sinks", "skin")
# False
# >>> is_anagram("Listen", "silent")
# True

# Make sure your function works with mixed case.

# Before you try to solve any bonuses, I recommend you try to find at least two ways to solve this problem.

# Okay now to the bonuses...

# Bonus 1

# For the first bonus, make sure your function ignores spaces ✔️:

# >>> is_anagram("coins kept", "in pockets")
# True

# Bonus 2

# For a second bonus, make sure your function also ignores punctuation ✔️:

# >>> is_anagram("a diet", "I'd eat")
# True

# Bonus 3

# If you solved this one really quickly, here's a more challenging third bonus for you: try allowing accented latin1 characters but ignoring the accent marks. ✔️

# >>> is_anagram("cardiografía", "radiográfica")
# True
import string
from unicodedata import normalize as norm

def is_anagram(str1, str2):
    no_acc1 = norm("NFKD", str1).encode("ascii", "ignore")
    no_acc2 = norm("NFKD", str2).encode("ascii", "ignore")
    no_punc1 = str(no_acc1).translate(str.maketrans('', '', string.punctuation))
    no_punc2 = str(no_acc2).translate(str.maketrans('', '', string.punctuation))
    return bool(sorted(list(no_punc1.lower().replace(" ",""))) == sorted(list(no_punc2.lower().replace(" ",""))))

print(is_anagram("coins kept","In Pockets"))
print(is_anagram("steve", "esteban"))


