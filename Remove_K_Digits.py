# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for c in num:
            while stack and k>0 and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        while stack and k>0:
            stack.pop()
            k -= 1
        if not stack:
            return "0"
        return str(int("".join(stack)))
        
