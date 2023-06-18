#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
'''

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def length(z):
            if z not in memo:
                memo[z] = 1 + max([length(Z)
                                   for Z in [z+1, z-1, z+1j, z-1j]
                                   if Z in matrix and matrix[z] > matrix[Z]]
                                  or [0])
            return memo[z]
        memo = {}
        matrix = {i + j*1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        return max(map(length, matrix), default = 0)
        
# @lc code=end

