#
# @lc app=leetcode id=1255 lang=python3
#
# [1255] Maximum Score Words Formed by Letters
#
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/
#
# algorithms
# Hard (82.11%)
# Likes:    1757
# Dislikes: 111
# Total Accepted:    119.3K
# Total Submissions: 145.7K
# Testcase Example:  '["dog","cat","dad","good"]\n' +
  '["a","a","c","d","d","d","g","o","o"]\n' +
  '[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]'
#
# Given a list of words, list of  single letters (might be repeating) and score
# of every character.
# 
# Return the maximum score of any valid set of words formed by using the given
# letters (words[i] cannot be used two or more times).
# 
# It is not necessary to use all characters in letters and each letter can only
# be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0],
# score[1], ... , score[25] respectively.
# 
# 
# Example 1:
# 
# 
# Input: words = ["dog","cat","dad","good"], letters =
# ["a","a","c","d","d","d","g","o","o"], score =
# [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with
# a score of 23.
# Words "dad" and "dog" only get a score of 21.
# 
# Example 2:
# 
# 
# Input: words = ["xxxz","ax","bx","cx"], letters =
# ["z","a","b","c","x","x","x"], score =
# [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# Output: 27
# Explanation:
# Score  a=4, b=4, c=4, x=5, z=10
# Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5)
# with a score of 27.
# Word "xxxz" only get a score of 25.
# 
# Example 3:
# 
# 
# Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score =
# [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# Output: 0
# Explanation:
# Letter "e" can only be used once.
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 14
# 1 <= words[i].length <= 15
# 1 <= letters.length <= 100
# letters[i].length == 1
# score.length == 26
# 0 <= score[i] <= 10
# words[i], letters[i] contains only lower case English letters.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_counts = Counter(letters)
        n = len(words)
        max_score = 0

        for i in range(1 << n):
            current_score = 0
            current_counts = Counter()
            for j in range(n):
                if (i >> j) & 1:
                    for char in words[j]:
                        current_counts[char] += 1
            
            valid = True
            for char in current_counts:
                if current_counts[char] > letter_counts[char]:
                    valid = False
                    break
            
            if valid:
                for char in current_counts:
                    current_score += current_counts[char] * score[ord(char) - ord('a')]
                max_score = max(max_score, current_score)
        
        return max_score
        
# @lc code=end

