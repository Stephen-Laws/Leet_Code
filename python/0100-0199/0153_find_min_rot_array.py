# https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) -1
        target = nums[-1]
        med = (lo+hi) //2
        while hi > lo:  
            if nums[med] == target:
                return med
            elif nums[med] < target:
                hi = med
            else:
                lo = med + 1
            med = (lo+hi) //2

        return nums[med]