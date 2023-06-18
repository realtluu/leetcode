#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left: 
                generate(p + '(', left-1, right)
            if right > left: 
                generate(p + ')', left, right-1)
            if not right:
                parens += p,
            return parens
        return generate('', n, n)
        
# @lc code=end

