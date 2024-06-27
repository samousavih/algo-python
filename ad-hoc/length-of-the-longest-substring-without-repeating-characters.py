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
    lastIndex = 0
    for index,c in enumerate(s):
        if c in map:
            
            maxLength = max(maxLength,index-lastIndex)
            map[c] = index
            lastIndex = index
        else:
            map[c] = index
    
    maxLength = max(maxLength,index-lastIndex)
    return maxLength
print(lengthOfLongestNoRepeat("ABCDEFGABEF"))
print(lengthOfLongestNoRepeat("ABCADEDFGABEF"))
print(lengthOfLongestNoRepeat("GEEKSFORGEEKS"))
        
