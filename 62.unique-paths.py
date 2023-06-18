#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if 1 in [n, m]: return 1
        return reduce(lambda x, y: x*y, range(n, n + m - 1)) // reduce(lambda x, y: x*y, range(1, m))
        
# @lc code=end

