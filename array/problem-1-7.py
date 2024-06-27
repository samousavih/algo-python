"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

[a11,a12,a21,a22] => [a21,a11,a22,a12]

a11 a12 a13 a14      a41 a31 a21 a11
a21 a22 a23 a24      a42 a32 a22 a12 
a31 a32 a33 a34      a43 a33 a23 a13
a41 a42 a43 a44      a44 a34 a24 a14

"""
def rotateMatrix90(matrix,n):

    for l in range(1,n//2):
        

