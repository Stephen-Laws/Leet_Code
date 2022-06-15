class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        hi = len(nums)
        lo = 0
        idx = (hi-lo)//2
        while hi > lo :
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                hi = idx
            else:
                lo = idx + 1
            idx = (hi-lo)//2 + lo
        return hi