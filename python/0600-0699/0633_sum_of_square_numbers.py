# https://oj.leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return self.twoPointer(c)
        
    def twoPointer(self, c: int) -> bool:
        n1 = int(sqrt(c)) + 1
        n2 = 0
        while n1 >= n2:
            if n1 * n1 + n2* n2 == c:
                return True
            elif n1*n1 + n2*n2 > c:
                n1 -= 1
            else:
                n2 += 1
        return False