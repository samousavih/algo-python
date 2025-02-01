"""
Given a string str, find the length of the longest substring without repeating characters. 

Example:

Example 1:
Input: “ABCDEFGABEF”
Output: 7
Explanation: The longest substring without repeating characters are “ABCDEFG”, “BCDEFGA”, and “CDEFGAB” with lengths of 7

Example 2:
Input: “GEEKSFORGEEKS”
Output: 7
Explanation: The longest substrings without repeating characters are “EKSFORG” and “KSFORGE”, with lengths of 7
"""
def lengthOfLongestNoRepeat(s):
    map = {}
    maxLength = 0
    start = 0
    for index,c in enumerate(s):
        if c in map and map[c] >= start :
            maxLength = max(maxLength,index-start)
            start = map[c] + 1    
        map[c] = index
    maxLength = max(maxLength,len(s)-start)
    return maxLength

assert lengthOfLongestNoRepeat("ABCDEFGABEF") == 7
assert lengthOfLongestNoRepeat("GEEKSFORGEEKS") == 7
assert lengthOfLongestNoRepeat("ABCADEDFGABEF") == 6
assert lengthOfLongestNoRepeat("BBBBBB") == 1
assert lengthOfLongestNoRepeat("PWWKEW") == 3
assert lengthOfLongestNoRepeat("DVDF") == 3
assert lengthOfLongestNoRepeat("") == 0
assert lengthOfLongestNoRepeat("A") == 1
assert lengthOfLongestNoRepeat("AB") == 2
assert lengthOfLongestNoRepeat("AA") == 1
# 
        
