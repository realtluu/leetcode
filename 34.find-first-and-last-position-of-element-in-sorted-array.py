#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        def bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def bisect_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l if nums[l] == target else -1

        return [bisect_left(nums, target), bisect_right(nums, target)]
        
# @lc code=end

