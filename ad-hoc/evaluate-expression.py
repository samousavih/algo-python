"""

Topics
Companies
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

"""
["2","1","+","3","*"]
time: o(n)
space : o(n)

"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tempStack = []
        while len(tokens) > 1:
            token = tokens.pop()
            if self.isOperator(token) and not self.isOperator(tokens[-1]) and not self.isOperator(tokens[-2]):
                    second = tokens.pop()
                    first = tokens.pop()
                    result = self.calculate(token,first,second)
                    tokens.append(result)
                    while len(tempStack)>0:
                        tokens.append(tempStack.pop())
            else:
                tempStack.append(token)
        return int(tokens[0])
    def isOperator(self,token):
        return token in ["+","-","*","/"]
    def calculate(self,token,first,second):
        if token == "+":
            return int(first)+int(second)
        if token == "-":
            return int(first)-int(second)
        if token == "*":
            return int(first)*int(second)
        if token == "/":
            return int(int(first)/int(second))

