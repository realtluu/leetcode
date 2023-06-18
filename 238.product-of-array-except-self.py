#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res= [1 for _ in range(n)]
        f,b = 1,1
        for i in range(n):
            res[i]*=f
            res[n-1-i]*=b
            f*=nums[i]
            b*=nums[n-1-i]
        return res
        
# @lc code=end

