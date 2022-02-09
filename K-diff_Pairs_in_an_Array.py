"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.
"""

from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = dict(Counter(nums))
        pairs = 0
        
        for items in freq:
            if k == 0:
                if freq[items] > 1:
                    pairs += 1
            else:
                if items + k in freq:
                    pairs += 1
        return pairs
