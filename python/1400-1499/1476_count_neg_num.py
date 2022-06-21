# https://oj.leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # count up and right from bottom left of array
        m = len(grid)-1
        n = len(grid[0])
        r = m
        c = 0
        count = 0
        while c < n:
            #print(r,c,grid[r][c],count)
            if grid[r][c] < 0 and r != -1:
                r -= 1
            else:
                c += 1
                count += m - r
        return count
    
                