# https://oj.leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:        
        hi = n
        lo = 1
        
        while hi>=lo:
            rows = (hi+lo)//2
            if ((rows*(rows+1))/2) <= n:
                lo = rows +1
                ans = rows
            else:
                hi = rows -1
        return ans