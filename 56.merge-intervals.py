#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for inter in intervals:
            
            # if merged is empty or no overlap
            if not merged or merged[-1][1] < inter[0]:
                merged.append(inter)
            else:     
                # found overlap
                last = merged.pop()
                
                start = min(last[0], inter[0])
                end = max(last[1], inter[1])

                merged.append([start,end])
           
        return merged
        
# @lc code=end

