#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        decreasingHeightStack, totalWaterTrapped = [], 0
        
        for i, v in enumerate(height):
            while len(decreasingHeightStack) > 0 and height[decreasingHeightStack[-1]] < v:
                bottomHeight = height[decreasingHeightStack.pop()]
                if len(decreasingHeightStack) == 0:
                    break
                leftUpperIndex = decreasingHeightStack[-1]
                heightDiff = min(height[leftUpperIndex], v) - bottomHeight
                width = i - leftUpperIndex - 1
                totalWaterTrapped += heightDiff * width
                
            decreasingHeightStack.append(i)
            
        return totalWaterTrapped
        
# @lc code=end

