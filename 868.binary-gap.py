#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        pre = dist = 0
        for i, c in enumerate(bin(n)[2:]):
            if c == "1":
                dist = max(dist, i - pre)
                pre = i
        return dist
        
# @lc code=end