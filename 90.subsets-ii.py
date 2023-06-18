#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        ans.add(tuple())
        
        for num in nums:
            newSubsets = set()
            for subset in ans:  # Iterate previous subsets from ans
                newSubsets.add(tuple(list(subset) + [num]))
            ans.update(newSubsets)  # Add new subsets to ans
			
        return ans
        
# @lc code=end

