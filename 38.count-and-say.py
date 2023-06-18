#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\2*)', s))
        return s    
        
# @lc code=end

