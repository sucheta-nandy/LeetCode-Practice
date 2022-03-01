"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
		# We have to decide whether to keep the third (array index 2) element or overwrite it and so on.
        write_index = 2
        for i in range(2, len(nums)):
		    # If the last two numbers in the array are the same as the current one, don't increment the write_index.
			# Our search for the next number to be added to the list continues.
            if nums[write_index - 2] == nums[write_index - 1] == nums[i]:
                continue
			# We have found a non duplicate, copy the number into the position of the write_index and increment it.
            nums[write_index] = nums[i]
            write_index += 1

        return write_index
