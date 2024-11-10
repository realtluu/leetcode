#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#
# https://leetcode.com/problems/unique-paths-iii/description/
#
# algorithms
# Hard (81.91%)
# Likes:    5195
# Dislikes: 191
# Total Accepted:    213.8K
# Total Submissions: 260.7K
# Testcase Example:  '[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]'
#
# You are given an m x n integer array grid where grid[i][j] could be:
# 
# 
# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# 
# 
# Return the number of 4-directional walks from the starting square to the
# ending square, that walk over every non-obstacle square exactly once.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# 
# 
# Example 3:
# 
# 
# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly
# once.
# Note that the starting and ending square can be anywhere in the grid.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# 1 <= m * n <= 20
# -1 <= grid[i][j] <= 2
# There is exactly one starting cell and one ending cell.
# 
# 
#

# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        start_row, start_col = -1, -1
        empty_cells = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_row, start_col = r, c
                elif grid[r][c] == 0:
                    empty_cells += 1

        self.paths = 0

        def backtrack(row, col, visited):
            if grid[row][col] == 2:
                if len(visited) == empty_cells + 1:  # +1 to include starting cell
                    self.paths += 1
                return

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    backtrack(nr, nc, visited)
                    visited.remove((nr, nc))

        visited = set() # Initialize visited as an empty set!!
        visited.add((start_row, start_col)) # Add starting cell only at the beginning of the backtrack
        backtrack(start_row, start_col, visited)
        return self.paths
        
# @lc code=end

