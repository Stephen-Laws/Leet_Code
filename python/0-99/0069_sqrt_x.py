# https://oj.leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x==2: 
            return 1
        hi = x
        lo = 1
        sqrt = (hi+lo)//2
        while hi > lo:
            if sqrt*sqrt <= x < (sqrt+1)*(sqrt+1):
                return sqrt
            elif sqrt*sqrt > x:
                hi = sqrt
            else:
                lo = sqrt+1
            sqrt = (hi+ lo) //2

        return sqrt