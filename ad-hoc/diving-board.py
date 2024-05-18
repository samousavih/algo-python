"""
You are building a diving board by placing a bunch of planks of wood end-to-end. There are two types of planks, one of length shorter and one of length longer.
You must use exactly K planks of wood. Write a method to generate all possible lengths for the diving board.

return all lengths in non-decreasing order.

Example:

Input: 

shorter = 1

longer = 2

k = 3

Output:  {3,4,5,6}

Note:

0 < shorter <= longer
0 <= k <= 100000

{1,1,1}
k=1  {1,2}
k=2  {2,3,4}
k=3  {3,4,5}
        4,5,6
k=4  {4,5,6,7
        5,6,7,8}
comb[k] = 
         for (i <= K )
          for x in {1,2} {
            for (comb in comb[k-1])
                set.add(comb+x) 
}
"""

from typing import List


def find_comb(shorter,longer,k):
    comb = [set() for i in range(k+1)]
    comb[1].add(longer)
    comb[1].add(shorter)
    for i in range(2,k+1):
        comb[i] = set()
        for x in [shorter,longer]:
            for com in comb[i-1]:
                comb[i].add(com+x)
    return comb[k]

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if longer == shorter:
            return [longer * k]
        ans = []
        for i in range(k + 1):
            ans.append(longer * i + shorter * (k - i))
        return ans

print(find_comb(1,2,3))
print(find_comb(1,1,3))