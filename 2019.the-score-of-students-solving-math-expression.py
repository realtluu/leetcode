#
# @lc app=leetcode id=2019 lang=python3
#
# [2019] The Score of Students Solving Math Expression
#

# @lc code=start
class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        n = len(s) // 2 + 1
        
        # initialize dp
        dp = [[set() for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i].add(int(s[i*2]))
            
        for length in range(1, n):
            for i in range(n-length):
                j = i + length
                for k in range(i, j):
                    op = s[2*k+1]
                    # the value range check is important, it will hit TLE otherwise
                    if op == '+':
                        dp[i][j].update([n1 + n2 for n1 in dp[i][k] for n2 in dp[k+1][j] if n1 + n2 <= 1000])
                    else:
                        dp[i][j].update([n1 * n2 for n1 in dp[i][k] for n2 in dp[k+1][j] if n1 * n2 <= 1000])
        
        correct = eval(s)
        res = 0
        for ans in answers:
            if ans == correct: res += 5
            elif ans in dp[0][-1]: res += 2
        return res
            
# @lc code=end

