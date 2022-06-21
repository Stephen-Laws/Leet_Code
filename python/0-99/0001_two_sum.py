# https://oj.leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results_dict = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in results_dict:
                return [i, results_dict[res]]
            else:
                results_dict[num] = i

