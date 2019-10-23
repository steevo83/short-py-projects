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

matrix1 = [[5,9,15], [-2,3,4], [11, 2]]
matrix2 = [[6,12,16], [9,8,-7], [10, 20]]
print(add(matrix1, matrix2))


### Original code ###
  # return [
  #   [item1+item2 for  item1, item2 in zip(row1, row2)]
  #   for row1, row2 in zip(matrix1, matrix2)
  # ]
  
# def add(matrix1, matrix2):
#     """Add corresponding numbers in given 2-D matrices."""
#     combined = []
#     for row1, row2 in zip(matrix1, matrix2):
#         row = []
#         for n, m in zip(row1, row2):
#             row.append(n + m)
#         combined.append(row)
#     return combined

### Need to be able to do any number of lists of 2 lists -- and need to raise an error if not the same shape ###

# def add(*matrices):
#   """Add corresponding numbers in given 2-D matrices."""
#   combined = []
#   for rows in zip(*matrices):
#     row=[]
#     for values in zip(*rows):
#       row.append(sum(values))
#     combined.append(row)
#   return combined