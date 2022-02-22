# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string ""

class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s: return ""
        
        s1,s2 = min(s),max(s)

        i = 0
        while i<len(s1):
            if s1[i] != s2[i]:
                return s1[:i]
            i += 1

        return s1
