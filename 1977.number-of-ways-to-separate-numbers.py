#
# @lc app=leetcode id=1977 lang=python3
#
# [1977] Number of Ways to Separate Numbers
#

'''
You wrote down many positive integers in a string called num. However, you realized that you forgot to add commas to seperate the different numbers. You remember that the list of integers was non-decreasing and that no integer had leading zeros.
Return the number of possible lists of integers that you could have written down to get the string num. Since the answer may be large, return it modulo 109 + 7.

Example 1:
Input: num = "327"
Output: 2
Explanation: You could have written down the numbers:
3, 27
327

Example 2:
Input: num = "094"
Output: 0
Explanation: No numbers can have leading zeros and all numbers must be positive.

Example 3:
Input: num = "0"
Output: 0
Explanation: No numbers can have leading zeros and all numbers must be positive.

Example 4:
Input: num = "9999999999999"
Output: 101
'''

# @lc code=start
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        def ranks(l):
            index = {v: i for i, v in enumerate(sorted(set(l)))}
            return [index[v] for v in l]

        def suffixArray(s):
            line = ranks(s)
            n, k, ans, sa = len(s), 1, [line], [0]*len(s)
            while k < n - 1:
                line = ranks(list(zip_longest(line, islice(line, k, None), fillvalue=-1)))
                ans, k = ans + [line], k << 1
            for i, k in enumerate(ans[-1]): sa[k] = i
            return ans, sa

        def compare(i, j, l, k):
            a = (c[k][i], c[k][(i+l-(1<<k))%n])
            b = (c[k][j], c[k][(j+l-(1<<k))%n])
            return 0 if a == b else 1 if a < b else -1

        c, sa = suffixArray([int(i) for i in s])

        n, M = len(s), 10**9 + 7
        dp = np.zeros([n+1, n+1], dtype = int) #[[0]*(n+1) for _ in range(n+1)]
        mp = np.zeros([n+1, n+1], dtype = int) #[[0]*(n+1) for _ in range(n+1)]

        for k in range(n+1):
            dp[0][k] = 1
            mp[0][k] = 1

        logs = [0] + [floor(log2(k)) for k in range(1, n+1)]

        s_zero = np.array([i != "0" for i in s], dtype = int)

        for i in range(1, n+1):
            dp[i][1:i+1] = mp[range(i-1,-1,-1), range(i)] * s_zero[i-1::-1]

            check1 = dp[range(i-1, (i-1)//2, -1), range(1, i//2 + 1)]
            f = lambda k: compare(i-2*k, i-k, k, logs[k]) >= 0
            check2 = np.array([f(i) for i in range(1, i//2+1)])

            dp[i][1:i//2+1] = dp[i][1:i//2+1] + check1*check2
            dp[i][1:i//2+1] = [x % M for x in dp[i][1:i//2+1]]

            mp[i] = np.cumsum(dp[i])

        return mp[-1][-1] % M
# @lc code=end

