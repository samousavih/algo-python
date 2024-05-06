"""
Given an array A of N elements. Find the majority element in the array.
A majority element in an array A of size N is an element that appears strictly more than N/2 times in the array.

Example 1:

Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.
Example 2:

Input:
N = 5 
A[] = {3,1,3,3,2} 
Output:
3
Explanation:
Since, 3 is present more
than N/2 times, so it is 
the majority element.

Your Task:
The task is to complete the function majorityElement() which returns the majority element in the array. If no majority exists, return -1.
 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 

Constraints:
1 ≤ N ≤ 107
0 ≤ Ai ≤ 106
"""
"""
{3,1,3,3,2}
[1,2,3,3,3]

[1,2,2,2,2,3,4]

find median
count how many equal to median if > N/2 true else false

"""

def majorityElement(arr):
    median = find_median(arr)
    count=0
    for a in arr:
        if a == median:
            count+=1
            if count > len(arr)/2:
                return median
    return -1

def find_median(arr):
    k= len(arr)//2
    low = 0
    hi = len(arr)-1

    while low <= hi:
        p = pivot(arr,low,hi)
        if k==p:
            return arr[p]
        elif k < p:
            hi = p-1
        else:
            low = p+1
    return arr[k]

def pivot(arr,start,end):
    k = start
    low = k+1
    hi = end
    while low <= hi:
        if arr[low] > arr[k] and arr[hi] < arr[k]:
            swap(arr,low,hi)
            low+=1
            hi-=1
        elif arr[low] < arr[k]:
            low+=1
        else:
            hi-=1
    swap(arr, k, low-1)
    return low-1

def swap(arr,i,j):
    temp = arr[j]
    arr[j] = arr[i]          
    arr[i] = temp

def test_majorityElement():
    arr = [3,1,3,3,2]
    assert majorityElement(arr) == 3
    arr = [1,2,3]
    assert majorityElement(arr) == -1
    arr =[3, 3, 4, 2, 4, 4, 2, 4, 4]
    assert majorityElement(arr) == 4

test_majorityElement()