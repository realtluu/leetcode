#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        c = len(grid)
        r = len(grid[0])    
        for i in range(c):
            for j in range(r):
                if i ==0 and j ==0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])              
        return grid[-1][-1]
        
# @lc code=end

