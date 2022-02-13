"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

# one-liner recursion solution
class Solution:
    def subsets(self, nums: List[int], subset=[]) -> List[List[int]]:
        return self.subsets(nums[1:], subset+[nums[0]]) + self.subsets(nums[1:], subset) if nums else [subset]
      

# dp solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dp = [[]]
        for n in nums:
            tmp = []
            for x in dp:
                tmp.append(x + [n])
            dp += tmp
        return dp
