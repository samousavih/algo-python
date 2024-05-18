"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys={}
        keys[2] = ["a","b","c"]
        keys[3] = ["d","e","f"]
        keys[4] = ["g","h","i"]
        keys[5] = ["j","k","l"]
        keys[6] = ["m","n","o"]
        keys[7] = ["p","q","r","s"]
        keys[8] = ["t","u","v"]
        keys[9] = ["w","x","y","z"]
        sofar=[]
        if len(digits) == 0:
            return []
        sofar = keys[int(digits[0])]
        for digit in digits[1:]:
            temp = []
            for letter in keys[int(digit)]:
                for existing in sofar:
                    temp.append(existing+letter)
            sofar = temp
        return sofar
    def letterCombinations2(self, digits: str) -> List[str]:
        keys={}
        keys[2] = ["a","b","c"]
        keys[3] = ["d","e","f"]
        keys[4] = ["g","h","i"]
        keys[5] = ["j","k","l"]
        keys[6] = ["m","n","o"]
        keys[7] = ["p","q","r","s"]
        keys[8] = ["t","u","v"]
        keys[9] = ["w","x","y","z"]
        
        if len(digits) == 0:
            return []
        result = []
        sofar=[]
        self.letterCombinationsRec(keys,digits,sofar,result)
        return result
        
    def letterCombinationsRec(self,keys,remainingDigits,sofar,result):
            if len(remainingDigits) == 0:
                result.append(sofar)
                return
            firstRemainingDigit = remainingDigits[0]
            for letter in keys[int(firstRemainingDigit)]:
                self.letterCombinationsRec(keys,remainingDigits[1:],sofar+[letter],result)

print(Solution().letterCombinations2(["2","3","4"]))
                