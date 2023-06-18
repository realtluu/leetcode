#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [ [0]*n for _ in range(m) ]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i==j==0: # dp[0][0]=1
                        dp[i][j] = 1
                        continue
                    else:         # hidden: [-1][j]=0 and dp[i][-1]=0 since dp = [ [0]*n for _ in range(m) ]
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]  
        
# @lc code=end

