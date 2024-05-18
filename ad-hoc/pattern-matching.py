"""
You are given two strings, pattern and value. The pattern string consists of just the letters a and b, describing a pattern within a string. For example, the string catcatgocatgo matches the pattern aabab (where cat is a and go is b). It also matches patterns like a, ab, and b. Write a method to determine if value matches pattern. a and b cannot be the same string.

Example 1:

Input:  pattern = "abba", value = "dogcatcatdog"


Output:  true


Example 2:

Input:  pattern = "abba", value = "dogcatcatfish"


Output:  false


Example 3:

Input:  pattern = "aaaa", value = "dogcatcatdog"


Output:  false


Example 4:

Input:  pattern = "abba", value = "dogdogdogdog"


Output:  true


Explanation:  "a"="dogdog",b=""，vice versa.


Note:

0 <= len(pattern) <= 1000
0 <= len(value) <= 1000
pattern only contains "a" and "b", value only contains lowercase letters.
"""


from collections import Counter


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        def check(la: int, lb: int) -> bool:
            i = 0
            a, b = "", ""
            for c in pattern:
                if c == "a":
                    if a and value[i : i + la] != a:
                        return False
                    a = value[i : i + la]
                    i += la
                else:
                    if b and value[i : i + lb] != b:
                        return False
                    b = value[i : i + lb]
                    i += lb
            return a != b

        n = len(value)
        cnt = Counter(pattern)
        if cnt["a"] == 0:
            return n % cnt["b"] == 0 and value[: n // cnt["b"]] * cnt["b"] == value
        if cnt["b"] == 0:
            return n % cnt["a"] == 0 and value[: n // cnt["a"]] * cnt["a"] == value

        for la in range(n + 1):
            if la * cnt["a"] > n:
                break
            lb, mod = divmod(n - la * cnt["a"], cnt["b"])
            if mod == 0 and check(la, lb):
                return True
        return False