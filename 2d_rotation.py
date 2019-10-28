
# Python3 program to rotate a matrix by 90 degrees 
N = 4
  
# An Inplace function to rotate  
# N x N matrix by 90 degrees in 
# anti-clockwise direction 
def rotateMatrix(mat, dir="left"): 
      
    # Consider all squares one by one 
    print(f'x in range(0, int({N}/2) <<<{int(N/2)}>>>)')
    for x in range(0, int(N/2)): 
        print(f'x: {x}')     
        # Consider elements in group    
        # of 4 in current square 
        print(f'y in range({x}, {N}-{x}-1 <<<{N-x-1}>>>)')
        for y in range(x, N-x-1):
            print(f'y: {y}')  
            # store current cell in temp variable  
            temp = mat[x][y]
            if dir == "left":  
                # move values from right to top 
                mat[x][y] = mat[y][N-1-x] 
    
                # move values from bottom to right 
                mat[y][N-1-x] = mat[N-1-x][N-1-y] 
    
                # move values from left to bottom 
                mat[N-1-x][N-1-y] = mat[N-1-y][x] 
    
                # assign temp to left 
                mat[N-1-y][x] = temp
            elif dir == "right":  
                # temp = mat[x][y]             
                # move values from right to *bottom* 
                mat[x][y] = mat[N-1-y][x]
    
                # move values from bottom to *left* 
                mat[y][N-1-x] = mat[N-1-y][x]
    
                # move values from left to *top*
                mat[N-1-x][N-1-y] = mat[y][N-1-x] 
    
                # assign temp to *right* 
                mat[N-1-x][N-1-y] = temp
  
  
# Function to pr the matrix 
def displayMatrix( mat ): 
      
    for i in range(0, N): 
          
        for j in range(0, N): 
              
            print (mat[i][j], end = ' ') 
        print ("") 
      
      
  
  
# Driver Code 
mat = [[0 for x in range(N)] for y in range(N)] 
  


# Test case 1 
mat = [ [1, 2, 3, 4 ], 
        [5, 6, 7, 8 ], 
        [9, 10, 11, 12 ], 
        [13, 14, 15, 16 ] ] 
          
rotateMatrix(mat) 
  
# Print rotated matrix 
displayMatrix(mat) 
print()

# Test case 2 
N=3

mat = [ [1, 2, 3 ], 
        [4, 5, 6 ], 
        [7, 8, 9 ] ] 
  
rotateMatrix(mat)

#Steve Test case 1
mat = [ ["tl","tm", "tr"], 
        ["ml","mm", "mr"],
        ["bl","bm","br"] ]

rotateMatrix(mat)
  
# Print rotated matrix 
displayMatrix(mat) 
print()

print("Rotate right")
rotateMatrix(mat, "right")
displayMatrix(mat) 
print()
rotateMatrix(mat, "test")
displayMatrix(mat) 
print()

# Test case 3 
N=2
mat = [ [1, 2 ], 
        [4, 5 ] ] 
          

  
rotateMatrix(mat) 
  
# Print rotated matrix 
displayMatrix(mat) 
  
  
# This code is contributed by saloni1297 
