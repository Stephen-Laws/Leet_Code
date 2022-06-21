# https://oj.leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)-1
        n = len(matrix[0]) -1
        bottom = m
        top = 0
        idx = (top+bottom) //2
        #find row
        while top <= bottom:
            if matrix[idx][0] <= target:
                top = idx + 1
            else: 
                bottom = idx-1
            idx = (top+bottom) //2
        
        left = 0
        right = n
        c_idx = (left+right)//2
        
        while left <= right:
            if matrix[idx][c_idx] == target:
                return True
            elif matrix[idx][c_idx] < target:
                left = c_idx+1
            else:
                right = c_idx-1
            c_idx = (left+right)//2
        return False
                