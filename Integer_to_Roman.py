"""
Given an integer, convert it to a roman numeral.
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        values = ['I','V','X','L','C','D','M']
        ans,i = '',0
        while num:
            digit = num%10
            if digit == 4: ans = values[i] + values[i + 1] + ans
            elif digit == 9: ans = values[i] + values[i + 2] + ans
            elif digit >= 5: ans = values[i+1] + values[i]*(digit-5) + ans
            else: ans = values[i]*digit + ans
            num //= 10
            i += 2
        return ans
