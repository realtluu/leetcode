#
# @lc app=leetcode id=1987 lang=python3
#
# [1987] Number of Unique Good Subsequences
#

# @lc code=start
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp, last = [1], {}
        for i, x in enumerate(binary):
            dp.append(dp[-1] * 2)
            dp[-1] -= dp[last[x]] if x in last else int(x == "0")
            dp[-1] = dp[-1] % (10**9 + 7)
            last[x] = i

        return dp[-1] - 1 + int("0" in binary)
        
# @lc code=end

