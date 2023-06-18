#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = collections.Counter(s[i:i+10] for i in range(0, len(s) - 9))
        return [key for key in counter if counter[key] > 1]
        
# @lc code=end

