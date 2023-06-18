#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def f(arr, k):
            if len(arr) == 1:
                return str(arr[0])
            count = math.factorial(len(arr)-1)
            for i in range(len(arr)):
                if count * i <= k <= count * (i+1):
                    return str(arr[i]) + f(arr[:i] + arr[i+1:], k-count * i)
                
        return f([i for i in range(1, 1+n)], k)
            
# @lc code=end

