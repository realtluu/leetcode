#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        res = []
        for i in sorted(intervals, key=lambda x:x.start):
            if res and res[-1].end >= i.start:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res
        
# @lc code=end

