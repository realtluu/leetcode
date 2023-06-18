#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
'''
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        csum = nums[0]
        for n in nums[1:]:
            csum = n if csum < 0 else csum + n
            if csum > max_sum:
                max_sum = csum
        return max_sum




# @lc code=end

