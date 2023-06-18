#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, H = 0, len(nums)
        while L < H:
            M = (L+H) // 2
            if target < nums[0] < nums[M]: # -inf
                L = M+1
            elif target >= nums[0] > nums[M]: # +inf
                H = M
            elif nums[M] < target:
                L = M+1
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1
        
# @lc code=end

