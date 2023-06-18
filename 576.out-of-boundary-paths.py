#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#

# @lc code=start
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        cur = [[0]*n for _ in range(m)]  # store current step's states
        cur[startRow][startColumn] = 1
        ans = 0
        for mm in range(maxMove):
            # for each possible move
            nxt = [[0]*n for _ in range(m)]  # store next step's states
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        # check its 4 neighbors
                        if 0 <= nr < m and 0 <= nc < n:
                            # if it is still in boundary
                            nxt[nr][nc] += val
                            nxt[nr][nc] %= MOD
                        else:
                            # if it is out of boundary
                            ans += val
                            ans %= MOD
            cur = nxt
        return ans

        
# @lc code=end

