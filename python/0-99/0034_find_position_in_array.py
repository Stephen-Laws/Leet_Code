# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        lo, hi = 0, len(nums) -1
        left = self.binSearch(nums,target,lo,hi, True)
        right = self.binSearch(nums,target,lo,hi, False)
        return [left, right]
        
    def binSearch(self, nums, target, lo, hi, left):
        result = -1
        while hi >= lo:
            idx = (hi+lo)//2

            if nums[idx] == target:
                if left:
                    hi = idx -1
                else:
                    lo = idx+ 1
                result = idx
            elif nums[idx] > target:
                hi = idx -1
            else:
                lo = idx+1
        return result  
        
            

    def searchRangeinefficient(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        lo, hi = 0, len(nums)-1
        mid = -1
        idx = (hi+lo)//2
        
        if hi == 0:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]

        while hi > lo:
            if nums[idx] == target:
                mid = idx
                break
            elif nums[idx] > target:
                hi = idx
            else: 
                lo = idx+1
            idx = (hi+lo)//2
        
        if nums[hi] == target:
            mid = hi
            
        if mid == -1:
            return [-1, -1]
        
        hi = mid
        lo =0
        idx = (hi+lo)//2
        while hi > lo:
            if nums[idx] == target: 
                hi = idx
            else:
                lo = idx + 1
            idx = (hi+lo)//2
        lower = idx
        
        lo = mid
        hi = len(nums)
        idx = (hi+lo)//2
        while hi > lo:
            print(hi, lo, idx, nums[idx])
            if nums[idx] == target: 
                lo = idx + 1
            else:
                hi = idx
            idx = (hi+lo)//2
        upper = idx-1        
        
        return [lower,upper]