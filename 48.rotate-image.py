#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotate_pos_clockwise(i,j):
            return j,self.n-1-i
    
        n = len(matrix)
        
        self.n = n
        
        if(n<=1): return
        for i in range((n+1)//2):
            for j in range(i,n-i-1):
                up_val = matrix[i][j]
                i_right,j_right = rotate_pos_clockwise(i,j)
                i_bottom,j_bottom = rotate_pos_clockwise(i_right,j_right)
                i_left,j_left = rotate_pos_clockwise(i_bottom,j_bottom)
                matrix[i][j] = matrix[i_left][j_left]
                matrix[i_left][j_left] = matrix[i_bottom][j_bottom]
                matrix[i_bottom][j_bottom] = matrix[i_right][j_right]
                matrix[i_right][j_right] = up_val
            
# @lc code=end

