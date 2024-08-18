"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

[a00,a01,a10,a11] => [a10,a00,a11,a01]

a00 a01 a02 a03      a30 a20 a10 a00
a10 a11 a12 a13      a31 a21 a11 a01 
a20 a21 a22 a23      a32 a22 a12 a02
a30 a31 a32 a33      a33 a23 a13 a03

This is done layer buy layer
"""
def rotateMatrix90(matrix,n):

    for l in range(n//2):
        for i in range(l,n-l-1):
            temp = matrix[l][i]
            matrix[l][i] = matrix[n-i-1][l]
            matrix[n-i-1][l] = matrix[n-l-1][n-i-1]
            matrix[n-l-1][n-i-1] = matrix[i][n-l-1]
            matrix[i][n-l-1] = temp


A = [[1, 2, 3, 4],
     [5, 6, 7, 8], 
     [9, 10, 11, 12], 
     [13, 14, 15, 16]]
rotateMatrix90(A,4)
print(A)
        

