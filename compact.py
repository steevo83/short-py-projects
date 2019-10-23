from itertools import groupby

def compact(iterable):
    return (item for item, group in groupby(iterable))


# def compact(seq):
#     compacted = []
#     #enumerate creates a tuple that includes the position as it's 0th index spot
#     previous = object()
#     for item in seq:
#         if item != previous:
#             compacted.append(item)
#             previous = item
#     return compacted
    
    # for pos, item in enumerate(seq):
    #     if pos == 0 or item != seq[pos-1]:
    #         compacted.append(item)
    #         print(f'{pos} {item}') 
    # return iter(compacted)
   


print(compact([1,1,2,3,5,2,6,6]))