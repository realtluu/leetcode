#
# @lc app=leetcode id=2014 lang=python3
#
# [2014] Longest Subsequence Repeated k Times
#

# @lc code=start
class Solution:

    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)
    
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        hot = "".join(el*(freq//k) for el, freq in Counter(s).items())
            
        combs = set()
        for l in range(len(hot) + 1):
            for cand in combinations(hot, l):
                for perm in permutations(cand):
                    combs.add("".join(perm))

        combs = sorted(combs, key = lambda x: (len(x), x), reverse = True)
        for c in combs:
            if self.isSubsequence(c*k, s):
                return c
        
# @lc code=end