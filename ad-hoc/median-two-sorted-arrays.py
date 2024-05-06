"""
Given two sorted arrays array1 and array2 of size m and n respectively. Find the median of the two sorted arrays.

Example 1:

Input:
m = 3, n = 4
array1[] = {1,5,9}
array2[] = {2,3,6,7}
Output: 5
Explanation: The middle element for
{1,2,3,5,6,7,9} is 5
Example 2:

Input:
m = 2, n = 4
array1[] = {4,6}
array2[] = {1,2,3,5}
Output: 3.5
Your Task:
The task is to complete the function MedianOfArrays() that takes array1 and array2 as input and returns their median. 

Can you solve the problem in expected time complexity?

Expected Time Complexity: O(min(log n, log m)).
Expected Auxiliary Space: O((n+m)/2).

Constraints: 
0 ≤ m,n ≤ 106
1 ≤ array1[i], array2[i] ≤ 109
"""

def MedianOfArrays(a,b):
    n = len(a)
    m = len(b)

    la = 0

    while True:
        ra = la+1
        lb = (n+m)//2 - la-2
        rb = (n+m)//2 - la-1    
        left_a = a[la] if la >=0 and la < len(a) else -float("inf") 
        right_a = a[ra] if ra >=0 and ra < len(a) else float("inf") 
        left_b = b[lb] if lb >=0 and lb < len(b) else -float("inf") 
        right_b = b[rb] if rb >=0 and rb < len(b) else float("inf") 
    

        if left_a <= right_b and left_b <= right_a:
            if (n+m)%2 == 0:
                return (max(left_a,left_b) + min(right_a,right_b))/2
            else:
                return min(right_a,right_b)
        elif left_a > right_b:
                la=-1      
        else:
                la=+1

def testMedianOfArrays():
    a = [4,6]
    b = [1,2,3,5]
    assert MedianOfArrays(a,b) == 3.5

    a = [1,5,9]
    b = [2,3,6,7]
    assert MedianOfArrays(a,b) == 5

testMedianOfArrays()








