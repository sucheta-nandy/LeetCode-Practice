"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return [] 
        prev, n, result, i = nums[0], len(nums), [], 1
	      # At ith index we decide for prev to nums[i-1]
        while i < n: 
            if nums[i] != nums[i-1] + 1:
                result.append(f"{prev}->{nums[i-1]}" if prev != nums[i-1] else f"{prev}") # Add the range or the individual value if start == end
                prev = nums[i] # Prev becomes current index i
            i += 1
        result.append(f"{prev}->{nums[i-1]}" if prev != nums[i-1] else f"{prev}") # Add the range or the individual value if start == end. This one is done as the last value or last range was left out.
        return result
