"""
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res, longest = len(intervals), 0
        srtd = sorted(intervals, key = lambda i: (i[0], -i[1]))
        
        for start, end in srtd:
            if end <= longest:
                res -= 1
            else:
                longest = end
                
        return res