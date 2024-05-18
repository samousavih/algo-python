"""
Smallest Difference pair of values between two unsorted Arrays

EXAMPLE
Input: {1, 3, 15, 11, 2}, {23, 127,235, 19, 8} 
Output: 3. That is, the pair (11, 8).
{1,2,3,11,15}
{8,19,23,127,235} 
[7,6,5,3,7,]
"""

def smallestDiff(a,b):
    a.sort()
    b.sort()
    i=j=0
    min=float('inf')
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            if abs(a[i] - b[j]) < min:
                min = abs(a[i] - b[j])
            i+=1
        elif a[i] > b[j]:
            if abs(a[i] - b[j]) < min:
                min = abs(a[i] - b[j])
            j+=1
        else:
            return 0
    return min

def testSmallestDiff():
    print(smallestDiff([1, 3, 15, 11, 2],[23, 127,235, 19, 8]))
        
testSmallestDiff()

