# https://oj.leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) ==1:
            return nums
        running_sum = [nums[0]]
        for i in range(1,len(nums)):
            running_sum.append(nums[i]+running_sum[i-1])
        return running_sum