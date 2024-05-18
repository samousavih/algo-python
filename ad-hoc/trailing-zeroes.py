"""
Write an algorithm which computes the number of trailing zeros in n factorial.
"""

class Solution:
    def trailingZeroes(self, N):
        #code here 
        count = 0
        while N >= 5:
            N = N // 5
            count += N
        return count
