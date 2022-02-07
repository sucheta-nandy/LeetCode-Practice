"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_cnt, t_cnt = Counter(s), Counter(t)
        for letter in t_cnt:
            if not s_cnt[letter] == t_cnt[letter]:
                return letter
