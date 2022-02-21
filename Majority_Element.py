"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class Solution:
	def majorityElement(self, nums: List[int]) -> int:

		frequency = {}

		result = nums[0]
		current_max_freq = 1

		for i in nums:

			if i not in frequency:
				frequency[i] = 1
			else:
				frequency[i] = frequency[i] + 1

				if frequency[i] > current_max_freq:
					result = i
					current_max_freq = frequency[i]

		return result
