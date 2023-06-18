#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
'''
Given two binary strings a and b, return their sum as a binary string.
'''

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, carry = '', 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            curval = (i >= 0 and a[i] == '1') + (j >= 0 and b[j] == '1')
            carry, rem = divmod(curval + carry, 2)
            res = str(rem) + res
            i -= 1
            j -= 1
        return res
        
# @lc code=end

