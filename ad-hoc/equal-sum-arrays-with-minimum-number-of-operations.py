"""
You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

 

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6
"""

import heapq


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        sum1 = 0
        for num in nums1:
            sum1+=num
        sum2 = 0
        for num in nums2:
            sum2+=num
        if sum1 == sum2:
            return 0
        
        max1 = len(nums1)*6
        min1 = len(nums1)*1
        max2 = len(nums2)*6
        min2 = len(nums2)*1

        if min1 > max2:
            return -1
        if min2 > max1:
            return -1
        
        commonMin = max(min1,min2)
        commonMax = min(max1,max2)

        
        middle = (sum1+sum2)//2

        if middle < commonMin:
            middle = commonMin

        if middle > commonMax:
            middle = commonMax
        
        nums1.sort()
        nums2.sort()
        moves = 0
        if sum1 > sum2:
            moves= self.countMoves(nums1,nums2,middle,sum1,sum2)           
        else:
            moves+= self.countMoves(nums2,nums1,middle,sum2,sum1)           
        return moves
    def countMoves(self,largerNums,smallerNums,middle,sum1,sum2):
        moves = 0
        leftSum = sum1 - middle
        for num in reversed(largerNums):
                if leftSum > 0:
                    if num-1 >= leftSum:
                        moves+=1
                        leftSum = 0
                    else:
                        leftSum-= num-1
                        moves+=1
            
        leftSum = middle - sum2
        for num in smallerNums:
            if leftSum > 0:
                if 6-num >= leftSum:
                    moves+=1
                    leftSum = 0
                else:
                    leftSum-= 6-num
                    moves+=1
        return moves


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2:
            s1, s2 = s2, s1
            nums1, nums2 = nums2, nums1
        # to make s1 < s2            
        heapq.heapify(nums1)            
        nums2 = [-num for num in nums2]
        heapq.heapify(nums2)            
        ans = 0
        diff = s2 - s1
        while diff > 0 and nums1 and nums2:
            a = 6 - nums1[0]
            b = - (1 + nums2[0])
            if a > b:
                heapq.heappop(nums1)                
                diff -= a
            else:
                heapq.heappop(nums2)                
                diff -= b
            ans += 1                
        while diff > 0 and nums1:            
            a = 6 - heapq.heappop(nums1)                
            diff -= a
            ans += 1                
        while diff > 0 and nums2:            
            b = - (1 + heapq.heappop(nums2))
            diff -= b
            ans += 1                
        return ans if diff <= 0 else -1