#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canPartition(largestSum):
            groups = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largestSum:
                    groups += 1
                    curSum = num
            return groups <= m

        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if canPartition(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
# @lc code=end

