#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#
'''
Given a positive integer n, you can apply one of the following operations:
If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.
'''

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn
        
# @lc code=end

