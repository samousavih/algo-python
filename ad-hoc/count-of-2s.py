"""
Count of 2s: Write a method to count the number of 2s that appear in all the numbers between O
and n (inclusive).
EXAMPLE
Input: 25
Output: 9 (2, 12, 20, 21, 22, 23, 24 and 25. Note that 22 counts for two 2s.)

4 (2)
6 (2) 

1) 2
2) 12, 2X, y2
3) xy2,x2y,2xy 1 is 2 + 2 is 2 + 3 is 2 

12 % 10  = 2 12//10  = 1  122 10 12 100 1  122/1000000
"""

def countOf2(n):
    i = 0
    count = 0
    while i <= n:
        divider = 0
        remain = i
        while remain > 0:
            remain = remain // 10**divider
            if remain % 10  == 2:
                count+=1
            divider+=1
        i+=1
    return count
def testCountOf2():
    assert countOf2(25) == 9
    assert countOf2(2) == 1
    assert countOf2(12) == 2
testCountOf2()

        

