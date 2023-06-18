#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [1,2]
        for i in range(2, n):
            new = dp[0]+dp[1]
            dp[0] = dp[1]
            dp[1] = new
        return dp[-1]
                
  

# @lc code=end

