"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    counters = [0]*26
    uniqChar = set()
    for c in p:
      counters[ord(c)-ord('a')] += 1
      uniqChar.add(c)
    
    res = []
    left, match = 0, 0
    for right in range(len(s)):
      if s[right] in uniqChar:
        counters[ord(s[right])-ord('a')] -= 1
        if counters[ord(s[right])-ord('a')] == 0:
          match += 1
        
      if match == len(uniqChar):
        res.append(left)
                 
      if right-left+1 >= len(p):
        if s[left] in uniqChar:
          if counters[ord(s[left])-ord('a')] == 0:
            match -= 1
          counters[ord(s[left])-ord('a')] += 1
        left += 1
    return res
