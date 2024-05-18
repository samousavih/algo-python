"""
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
 

Follow up: Can you solve it in O(n) time complexity?
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = -1
        end = -1
        index = 0
        while index < len(nums)-1 and start == -1:
            if nums[index] > nums[index+1]:
                start = index
            index+=1
        index = len(nums)-1        
        while index > 0 and end == -1:
            if nums[index] < nums[index-1]:
                end = index
            index-=1

        
        if start < end:
            maxMiddle = -float('inf')
            minMiddle = float('inf')
            i = start
            while i <= end:
                  minMiddle = min(minMiddle,nums[i])
                  maxMiddle = max(maxMiddle,nums[i])
                  i+=1
            while end < len(nums)-1 and maxMiddle > nums[end+1]:
                end+=1
            while start > 0 and minMiddle < nums[start-1]:
                start-=1
            return end-start+1
        else:
            return 0