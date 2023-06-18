#
# @lc app=leetcode id=2040 lang=python3
#
# [2040] Kth Smallest Product of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        A1,A2 = [-a for a in nums1 if a < 0][::-1], [a for a in nums1 if a >= 0]
        B1,B2 = [-a for a in nums2 if a < 0][::-1], [a for a in nums2 if a >= 0]

        neg = len(A1) * len(B2) + len(A2) * len(B1)
        if k > neg:
            k -= neg
            s = 1
        else:
            k = neg - k + 1
            B1, B2 = B2,B1
            s = -1

        def count(nums1, nums2, x):
            res = 0
            j = len(nums2) - 1
            for i in range(len(nums1)):
                while j >= 0 and nums1[i] * nums2[j] > x:
                    j -= 1
                res += j + 1
            return res

        left, right = 0, 10**10
        while left < right:
            mid = (left + right) // 2
            if count(A1, B1, mid) + count(A2, B2, mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left * s

        
# @lc code=end

