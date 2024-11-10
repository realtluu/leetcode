#
# @lc app=leetcode id=2392 lang=python3
#
# [2392] Build a Matrix With Conditions
#
# https://leetcode.com/problems/build-a-matrix-with-conditions/description/
#
# algorithms
# Hard (79.58%)
# Likes:    1374
# Dislikes: 51
# Total Accepted:    93.3K
# Total Submissions: 117.3K
# Testcase Example:  '3\n[[1,2],[3,2]]\n[[2,1],[3,2]]'
#
# You are given a positive integer k. You are also given:
# 
# 
# a 2D integer array rowConditions of size n where rowConditions[i] = [abovei,
# belowi], and
# a 2D integer array colConditions of size m where colConditions[i] = [lefti,
# righti].
# 
# 
# The two arrays contain integers from 1 to k.
# 
# You have to build a k x k matrix that contains each of the numbers from 1 to
# k exactly once. The remaining cells should have the value 0.
# 
# The matrix should also satisfy the following conditions:
# 
# 
# The number abovei should appear in a row that is strictly above the row at
# which the number belowi appears for all i from 0 to n - 1.
# The number lefti should appear in a column that is strictly left of the
# column at which the number righti appears for all i from 0 to m - 1.
# 
# 
# Return any matrix that satisfies the conditions. If no answer exists, return
# an empty matrix.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
# Output: [[3,0,0],[0,0,1],[0,2,0]]
# Explanation: The diagram above shows a valid example of a matrix that
# satisfies all the conditions.
# The row conditions are the following:
# - Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the
# matrix.
# - Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the
# matrix.
# The column conditions are the following:
# - Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in
# the matrix.
# - Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in
# the matrix.
# Note that there may be multiple correct answers.
# 
# 
# Example 2:
# 
# 
# Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions =
# [[2,1]]
# Output: []
# Explanation: From the first two conditions, 3 has to be below 1 but the third
# conditions needs 3 to be above 1 to be satisfied.
# No matrix can satisfy all the conditions, so we return the empty matrix.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= k <= 400
# 1 <= rowConditions.length, colConditions.length <= 10^4
# rowConditions[i].length == colConditions[i].length == 2
# 1 <= abovei, belowi, lefti, righti <= k
# abovei != belowi
# lefti != righti
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions):
            graph = defaultdict(list)
            indegree = [0] * (k + 1)
            for above, below in conditions:
                graph[above].append(below)
                indegree[below] += 1

            queue = [node for node in range(1, k + 1) if indegree[node] == 0]
            order = []
            while queue:
                node = queue.pop(0)
                order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            return order if len(order) == k else []

        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)

        if not row_order or not col_order:
            return []

        matrix = [[0] * k for _ in range(k)]
        row_positions = {node: i for i, node in enumerate(row_order)}
        col_positions = {node: i for i, node in enumerate(col_order)}

        for i in range(1, k + 1):
            matrix[row_positions[i]][col_positions[i]] = i

        return matrix
        
# @lc code=end

