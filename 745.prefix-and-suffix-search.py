#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#

# @lc code=start
class WordFilter:

    def __init__(self, words: List[str]):
        """
        :type words: List[str]
        """
        self.ht = {}

        for W, w in enumerate(words):
            pre = ""
            L = len(w)
            for i in range(-1, min(10, L)): # first i letters form the prefix
                suf = ""
                if i != -1:
                    pre += w[i]
                for j in range(-1, min(10, L)): # last j letters form the suffix
                    if j != -1:                              
                        suf += w[-(j+1)]
                    self.ht[pre + "$" + suf] = W
        

    def f(self, prefix: str, suffix: str) -> int:
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        key = prefix + "$" + suffix[::-1]
        if key not in self.ht:
            return -1
        return self.ht[key]
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# @lc code=end