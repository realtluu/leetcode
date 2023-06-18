#
# @lc app=leetcode id=2057 lang=python3
#
# [2057] Smallest Index With Equal Value
#

# @lc code=start
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        return next((i for i, x in enumerate(nums) if i%10 == x), -1)

        
# @lc code=end

