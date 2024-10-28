#
# @lc app=leetcode id=488 lang=python3
#
# [488] Zuma Game
#
# https://leetcode.com/problems/zuma-game/description/
#
# algorithms
# Hard (32.60%)
# Likes:    460
# Dislikes: 496
# Total Accepted:    24.7K
# Total Submissions: 76.6K
# Testcase Example:  '"WRRBBW"\n"RB"'
#
# You are playing a variation of the game Zuma.
# 
# In this variation of Zuma, there is a single row of colored balls on a board,
# where each ball can be colored red 'R', yellow 'Y', blue 'B', green 'G', or
# white 'W'. You also have several colored balls in your hand.
# 
# Your goal is to clear all of the balls from the board. On each turn:
# 
# 
# Pick any ball from your hand and insert it in between two balls in the row or
# on either end of the row.
# If there is a group of three or more consecutive balls of the same color,
# remove the group of balls from the board.
# 
# If this removal causes more groups of three or more of the same color to
# form, then continue removing each group until there are none
# left.
# 
# 
# If there are no more balls on the board, then you win the game.
# Repeat this process until you either win or do not have any more balls in
# your hand.
# 
# 
# Given a string board, representing the row of balls on the board, and a
# string hand, representing the balls in your hand, return the minimum number
# of balls you have to insert to clear all the balls from the board. If you
# cannot clear all the balls from the board using the balls in your hand,
# return -1.
# 
# 
# Example 1:
# 
# 
# Input: board = "WRRBBW", hand = "RB"
# Output: -1
# Explanation: It is impossible to clear all the balls. The best you can do is:
# - Insert 'R' so the board becomes WRRRBBW. WRRRBBW -> WBBW.
# - Insert 'B' so the board becomes WBBBW. WBBBW -> WW.
# There are still balls remaining on the board, and you are out of balls to
# insert.
# 
# Example 2:
# 
# 
# Input: board = "WWRRBBWW", hand = "WRBRW"
# Output: 2
# Explanation: To make the board empty:
# - Insert 'R' so the board becomes WWRRRBBWW. WWRRRBBWW -> WWBBWW.
# - Insert 'B' so the board becomes WWBBBWW. WWBBBWW -> WWWW -> empty.
# 2 balls from your hand were needed to clear the board.
# 
# 
# Example 3:
# 
# 
# Input: board = "G", hand = "GGGGG"
# Output: 2
# Explanation: To make the board empty:
# - Insert 'G' so the board becomes GG.
# - Insert 'G' so the board becomes GGG. GGG -> empty.
# 2 balls from your hand were needed to clear the board.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= board.length <= 16
# 1 <= hand.length <= 5
# board and hand consist of the characters 'R', 'Y', 'B', 'G', and 'W'.
# The initial row of balls on the board will not have any groups of three or
# more consecutive balls of the same color.
# 
# 
#

# @lc code=start
from collections import Counter
from functools import lru_cache  # For memoization

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand_count = Counter(hand)

        def removeConsecutive(s):
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    s = s[:i] + s[j:]
                    i = 0
                else:
                    i = j
            return s

        @lru_cache(maxsize=None)  # Memoize results
        def solve(board, hand_tuple):
            if not board:
                return 0

            if not hand_tuple:
                return -1
            
            res = float('inf')
            for i in range(len(board) + 1):
                for color in hand_count:
                    if hand_tuple[ord(color) - ord('A')] > 0:
                        new_hand_tuple = list(hand_tuple)
                        new_hand_tuple[ord(color) - ord('A')] -= 1
                        new_hand_tuple = tuple(new_hand_tuple)

                        new_board = board[:i] + color + board[i:]
                        new_board = removeConsecutive(new_board)
                        sub_res = solve(new_board, new_hand_tuple)


                        if sub_res != -1:
                            res = min(res, sub_res + 1)

            return res if res != float('inf') else -1


        hand_tuple = tuple(hand_count.get(chr(i + ord('A')), 0) for i in range(26)) # Convert hand to a tuple for hashing
        return solve(board, hand_tuple)
        
# @lc code=end

