#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If we have only one row then we can return the string as it is
        if numRows < 2:
            return s
        result = [""] * numRows
        row = 0

        for character in s:
            # if we reach top we have to move down
            if row == 0:
                move_down = True
            # if we reach bottom then we have to move up
            elif row == numRows - 1:
                move_down = False

            # Add character to corresponding row
            result[row] += character

            # update the row -> increment by 1 if we move down else, decrement by 1 if we move up.
            row = (row + 1) if move_down else row - 1

        # Finally join all rows and return
        return "".join(result)
        
# @lc code=end

