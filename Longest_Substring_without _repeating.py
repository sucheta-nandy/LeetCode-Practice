"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] >= start:
                    start = d[s[i]] + 1
                    d[s[i]] = i
                else:
                    d[s[i]] = i
            else:
                d[s[i]] = i   
            ans = max(ans,i - start + 1)
        return ans
