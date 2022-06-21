# https://oj.leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubles = {}
        for i in arr:
            if i in doubles:
                return True
            else:
                doubles[2*i] = 1
                if i % 2 ==0:
                    doubles[i//2] = 1
        return False