#
# @lc app=leetcode id=2053 lang=python3
#
# [2053] Kth Distinct String in an Array
#

# @lc code=start
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr = [i for i in arr if arr.count(i) == 1]
        return "" if k > len(arr) else arr[k - 1]
        
# @lc code=end

