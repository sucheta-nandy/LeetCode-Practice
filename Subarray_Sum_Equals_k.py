"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0:1}
        ts = 0
        res = 0

        for n in nums:
            ts+=n
            if (ts-k in dct):
                res+=dct[ts-k]
            if ts in dct:
                dct[ts]+=1
            else: dct[ts]=1
        
        return res
