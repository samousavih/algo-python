"""
Letters and Numbers: Given an array filled with letters and numbers, find the longest subarray with
an equal number of letters and numbers.

[1,2,a,2,2,a,a] 
[0:1,1:2,2:1,3:2,4:3,5:2,6:1]
(diff:index)

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
        else:
            lastDiff[diff] = index
    return maxSubarry
def testLettersAndNumbers():
    assert lettersAndNumbers("12ab2cc") == 6
    assert lettersAndNumbers("12abcc2") == 4
    assert lettersAndNumbers("a1b2c3") == 6
    assert lettersAndNumbers("abc123") == 6
    assert lettersAndNumbers("123abc") == 6
    assert lettersAndNumbers("a1b2c") == 4
    assert lettersAndNumbers("1a2b3c4d") == 8
    assert lettersAndNumbers("abcd") == 0
    assert lettersAndNumbers("1234") == 0
    assert lettersAndNumbers("123a4a4a4a4") == 8
    assert lettersAndNumbers("123a4a4a4aa") == 10
testLettersAndNumbers()