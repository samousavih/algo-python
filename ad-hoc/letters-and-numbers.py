"""
Letters and Numbers: Given an array filled with letters and numbers, find the longest subarray with
an equal number of letters and numbers.

[1,2,a,b,2,c,c]  [1,2,a,b,c,c,2]
{1:0,2:1,3:0,4:-1,5:-2}
d-l
d : 3
l : 4

"""
def lettersAndNumbers(array):
    lastDiff = {}
    lastDiff[0] = -1
    diff = 0
    maxSubarry = 0
    for index,a in enumerate(array):
        if a.isnumeric():
            diff+=1
        else:    
            diff-=1
        if diff in lastDiff:
            maxSubarry = max(maxSubarry,index - lastDiff[diff])
    return maxSubarry
def testLettersAndNumbers():
    assert lettersAndNumbers("12ab2cc") == 6
    assert lettersAndNumbers("12abcc2") == 4
testLettersAndNumbers()