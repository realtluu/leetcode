#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
'''
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

We can just split our string, remove all extra spaces and return length of the last word, however we need to spend O(n) time for this, where n is length of our string. There is a simple optimization: let us traverse string from the end and:

find the last element of last word: traverse from the end and find first non-space symbol.
continue traverse and find first space symbol (or beginning of string)
return end - beg.

'''
# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end > 0 and s[end] == " ": end -= 1
        beg = end
        while beg >= 0 and s[beg] != " ": beg -= 1
        return end - beg
        
# @lc code=end

