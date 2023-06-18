#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
                '8':"tuv", '9':"wxyz"}
        cmb = [''] if digits else []
        for d in digits:
            cmb = [p + q for p in cmb for q in dict[d]]
        return cmb
        
# @lc code=end

