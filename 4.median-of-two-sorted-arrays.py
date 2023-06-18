#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        if len(nums)%2 == 0:
            return (nums[len(nums)//2-1]+nums[len(nums)//2])/2.0
        else:
            return nums[(len(nums)-1)//2]
        
# @lc code=end