# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
		# Edge Condition
        if len(s1) > len(s2):
            return False
        n1 = len(s1)
        
		# Hashmap for s1
        c1 = Counter(s1)
		
        for i in range(len(s2)-n1+1):
            if Counter(s2[i:i+n1]) == c1:
                       return True
        return False
