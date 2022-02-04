"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maps={0:-1}
        cummSum=maxSoFar=0
        for i,num in enumerate(nums):
            if num==1:
                cummSum+=1
            else:
                cummSum-=1
            if cummSum in maps:
                maxSoFar=max(maxSoFar,i-maps[cummSum])
            else:
                maps[cummSum] = i
        return maxSoFar
