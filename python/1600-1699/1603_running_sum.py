# https://oj.leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        curr = 0
        for num in nums:
            curr += num
            running_sum.append(curr)
        return running_sum