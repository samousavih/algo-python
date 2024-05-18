"""
Write a method that finds the maximum of two numbers. You should not use if-else
16.5
16.7
or any other comparison operator.

a b
"""

def max(a,b):
    d= [b,a]
    c= (((a-b)/abs(a-b))+1)/2
    return d[int(c)]

def greater_of_two(x, y):
    # mid-point
    return (abs(x - y) + (x + y)) // 2

print(max(16.5,16.7))
print(max(16.5,0))

