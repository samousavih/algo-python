"""
Given an unsorted array arr of positive integers. One number a from the set [1, 2,....,n] is missing and one number b occurs twice in the array. Find numbers a and b.

Note: The test cases are generated such that there always exists one missing and one repeating number within the range [1,n].

Examples:
Input: arr[] = [2, 2]
Output: [2, 1]
Explanation: Repeating number is 2 and smallest positive missing number is 1.
Input: arr[] = [1, 3, 3] 
Output: [3, 2]
Explanation: Repeating number is 3 and smallest positive missing number is 2.
Input: arr[] = [4, 3, 6, 2, 1, 1]
Output: [1, 5]
Explanation: Repeating number is 1 and the missing number is 5.

Constraints:
2 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size()


[5,4,3,3,1]
"""

class Solution1:
    def findTwoElement( self,arr): # O(N)
        n = 0
        duplicated = -1
        while n < len(arr):
            if arr[n] != n+1:
                if arr[arr[n]-1] == arr[n]:
                    duplicated = arr[n]
                    n+=1
                else:
                    self.swap(arr[n], arr[arr[n]-1])
            else:
                n+=1
        for index, n in enumerate(arr):
            if n != index+1:
                missing = index+1
        return [duplicated, missing]
    def swap(self,a,b):
        a,b = b,a


class Solution2:   # time : O(N) and space: O(N)  , but this one is quicker 
    def findTwoElement( self,arr): 
        n = 0
        duplicated = -1
        visited = set()
        sum = 0
        for n in arr:
            if n in visited:
                duplicated = n
            else:
                sum+=n
                visited.add(n)
        
                
        return [duplicated,int((len(arr)*(len(arr)+1))/2) - sum ] # O(1) to find missing