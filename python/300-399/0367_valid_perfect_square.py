# https://oj.leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1:
            return True
        hi = num
        lo = 1
        n = (hi+lo) // 2
        while hi > lo:
            if n*n > num:
                hi = n
            elif n*n < num:
                lo = n+1
            else:
                return True
            n = (hi+lo)//2
        return False