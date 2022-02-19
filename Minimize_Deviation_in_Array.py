"""
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.
"""

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        maxnums = [-(n * 2 if n & 1 else n) for n in nums] #To quickly pick the largest number we use min heap (therefore the nums in maxnums are negated).
        minn, maxx = -max(maxnums), -min(maxnums)
        mindev = maxx - minn

        heapq.heapify(maxnums)
        while not maxnums[0] & 1:
            maxtrans = maxnums[0] >> 1
            heapq.heapreplace(maxnums, maxtrans)
            minn = min(minn, -maxtrans)
            maxx = -maxnums[0]
            mindev = min(mindev, maxx - minn)

        return mindev
