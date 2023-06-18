#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        dp = [False]*(np+1)
           
        for si in range(ns+1):
            new_dp = [si == 0] + [False]*np
            for pi in range(1, np+1):
                if si>0 and p[pi-1] in [s[si-1], '?']:
                    new_dp[pi] = dp[pi-1]
                elif p[pi-1] == '*':
                    new_dp[pi] = dp[pi-1] or dp[pi] or new_dp[pi-1]
            dp = new_dp

        return dp[-1]
        
# @lc code=end

