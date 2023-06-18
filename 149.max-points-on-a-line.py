#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        counter = collections.Counter(map(tuple, points))
        points = list(counter.keys())
        max_so_far = 0
        for i in range(len(points)):
            x1, y1 = points[i]
            lines = {}
            for j in range(i):
                x2, y2 = points[j]
                slope = float('inf')
                if x1 != x2:
                    slope = (y2 - y1) / (x2 - x1)
                if slope in lines:
                    lines[slope] += counter[points[j]]
                else:
                    lines[slope] = counter[points[i]] + counter[points[j]]
            max_so_far = max(max_so_far, counter[points[i]], *lines.values())
        return max_so_far
        
# @lc code=end

