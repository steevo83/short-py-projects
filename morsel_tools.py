import string
from unicodedata import normalize as norm
from collections import defaultdict as ddict
from collections import OrderedDict as OD
import re
import operator
from itertools import groupby

def compact(iterable):
    return (item for item, group in groupby(iterable))


def add(*matrices):  
  matrix_shapes = {
    tuple(len(r) for r in matrix)
    for matrix in matrices
  }
  if len(matrix_shapes) > 1:
    raise ValueError("Given matrices are not the same size.")
  return [
    [sum(values) for values in zip(*rows)]
    for rows in zip(*matrices)
  ]


def is_anagram(str1, str2):
    no_acc1 = norm("NFKD", str1).encode("ascii", "ignore")
    no_acc2 = norm("NFKD", str2).encode("ascii", "ignore")
    no_punc1 = str(no_acc1).translate(str.maketrans('', '', string.punctuation))
    no_punc2 = str(no_acc2).translate(str.maketrans('', '', string.punctuation))
    return bool(sorted(list(no_punc1.lower().replace(" ",""))) == sorted(list(no_punc2.lower().replace(" ",""))))


def count_words(text):
    final = ddict(int)
    strip_punc = re.sub(r"[^\w\d'\s]","",text).split()
    for each in strip_punc:
        final[each.lower()] += 1
    final_ordered = sorted(final.items(), key=lambda kv:kv[1], reverse=True)
    return OD(final_ordered)


def get_earliest(*dates):
    split_list = []
    for breaks in dates:
        split_list.append(breaks.split("/"))
    sort = sorted(split_list, key = operator.itemgetter(2, 0, 1))
    return "/".join(sort[0])


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


####GROUP BY####
def mod(n, mod):
    return n%mod

def mult(n, mod):
    return n*mod

def group_by(numbers, key_func=lambda n, mod: n, mod_num=0):
    dd = ddict(list)
    for num in numbers:
        dd[key_func(num, mod_num)].append(num)
    return dd
########