# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: 
            return s
        window,start = 1,0
        start = 0
        for i in range(1, len(s)):
            if i - window >= 0 and s[i-window:i+1] == s[i-window:i+1][::-1]:
                start = i-window
                window += 1
            elif i-window >= 1 and s[i-window-1:i+1] == s[i-window-1:i+1][::-1]:
                start = i-window-1
                window += 2
        return s[start:start+window]
