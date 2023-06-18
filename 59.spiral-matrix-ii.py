#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """ 
        :type n: int
        :rtype: List[List[int]]
        """
        res, lo = [[n*n]], n*n 
        while lo > 1:
            lo, hi = lo - len(res), lo
            #print('res:', res)
            res = [[i for i in range(lo, hi)]] + [list(j) for j in zip(*res[::-1])]
        return res 
        
# @lc code=end

