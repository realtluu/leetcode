#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from functools import cache

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(left, right):
            if left<right:
                return [TreeNode(root, leftNode, rightNode) 
                        for root in range(left, right+1) 
                        for leftNode in dfs(left, root-1) for rightNode in dfs(root+1, right)]
            elif left!=right: 
                return [None]
            else: 
                return [TreeNode(left)]
        
        return dfs(1, n)
        
# @lc code=end

