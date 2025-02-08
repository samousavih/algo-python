"""
Given an array of positive integers, the task is to determine if a Pythagorean triplet exists in the given array. A triplet {a, b, c} is considered a Pythagorean triplet if it satisfies the condition a2 + b2 = c2.

Example:

Input: arr[] = {3, 1, 4, 6, 5} 
Output: True
Explanation: The array contains a Pythagorean triplet {3, 4, 5}.


Input: arr[] = {10, 4, 6, 12, 5} 
Output: False 
Explanation: There is no Pythagorean triplet. 
"""

def Pythagorean_triplet(arr):
    hashSet = set()
    for n in arr:
        hashSet.add(n**2)
    for n in arr:
        for m in arr:
            if n**2 + m**2 in hashSet:
                return True
    return False 

import math

def Pythagorean_triplet_2(arr):
    maxNumber = 0
    for n in arr:
        maxNumber = max(maxNumber,n)

    visited = [False] * (maxNumber+1)
    for n in arr:
        visited[n] = True
    for n in range(1,maxNumber+1):
        for m in range(1,maxNumber+1):
            if visited[n] and visited[m]:
                c = int(math.sqrt(n**2 + m**2))
                if n**2 + m**2 == c**2 and c < maxNumber and visited[c]:
                    return True
    return False 



def Test_Pythagorean_triplet():
    arr = [3, 1, 4, 6, 5]
    assert Pythagorean_triplet(arr) == True

    arr = [10, 4, 6, 12, 5]
    assert Pythagorean_triplet(arr) == False

    arr = [3, 1, 4, 6, 5]
    assert Pythagorean_triplet_2(arr) == True

    arr = [10, 4, 6, 12, 5]
    assert Pythagorean_triplet_2(arr) == False


Test_Pythagorean_triplet()