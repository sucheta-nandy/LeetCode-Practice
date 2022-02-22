"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle) - 1
        result = 0
        for ch in columnTitle:
            result += (26**n)*(ord(ch)-64)
            n-=1
        return result
