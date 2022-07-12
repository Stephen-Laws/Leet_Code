# https://oj.leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        ret = []
        for num in nums:
            summ += num
            ret.append(summ)
        return ret