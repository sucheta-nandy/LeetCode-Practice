"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxarea = 0
        
        while l < r:
            height_l, height_r = height[l], height[r]

            if height_l <= height_r:
                maxarea = max(maxarea, (r - l) * height_l)
                while height_l >= height[l] and l < r: l += 1
            else:
                maxarea = max(maxarea, (r - l) * height_r)
                while height_r >= height[r] and l < r: r -= 1

        return maxarea
