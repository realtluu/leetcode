#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
            
# @lc code=end

