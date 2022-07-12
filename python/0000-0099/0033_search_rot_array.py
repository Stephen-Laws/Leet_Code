# https://oj.leetcode.com/problems/search-in-rotated-sorted-array/

class Solution: 
    def search(self, nums: List[int], target: int) -> int:
        return self.efficient_search(nums,target)

    def efficient_search(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # if found target value, return the index
            if nums[mid] == target:
                return mid
            
            # determine it's left rotated or right rotated
            """
            No rotated:
            1 2 3 4 5 6 7
                 mid
                 
            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
            
            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
            """
            if nums[mid] >= nums[left]: # left rotated
                # in ascending order side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right rotated
                # in ascending order side
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # cannot find the target value
        return -1
            
    def inefficient_binary(self, nums: List[int], target: int) -> int:
        pivot = 1
        if nums[0] < nums[-1]:
            pivot = 0
        
        lo = 1
        hi = len(nums) - 1
        idx = (hi + lo) // 2

        while pivot and hi > lo:
            if nums[idx] < nums[-1]:
                hi = idx
            else: 
                lo = idx + 1
            idx = (hi + lo) // 2

        if target > nums[-1] and pivot:
            lo = 0
            hi = idx -1
        elif target< nums[-1] and pivot:
            lo = idx
            hi = len(nums) -1
        elif pivot:
            return len(nums) -1
        else:
            lo = 0
            hi = len(nums) -1
        
        idx = (hi + lo)//2

        while hi>lo:
            if nums[idx] >= target: 
                hi = idx
            else:
                lo = idx + 1
            idx = (hi+lo) // 2
        return -1 if nums[idx] != target else idx