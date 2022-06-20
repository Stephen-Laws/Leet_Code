# https://oj.leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hi = len(numbers)-1
        lo = 0
        idx = (hi+lo) // 2
        while hi > lo:
            if numbers[idx]+numbers[idx+1] <= target:
                lo = idx + 1
            else: 
                hi = idx
            idx = (lo+hi)//2
            print(hi, lo, idx)
        hi_idx = idx
        lo_idx = idx-1
        curr_sum = numbers[lo_idx] + numbers[hi_idx]
        while curr_sum != target:
            if curr_sum > target:
                lo_idx -= 1
            else:
                hi_idx += 1
            curr_sum = numbers[lo_idx] + numbers[hi_idx]
        return [lo_idx+1, hi_idx+1]