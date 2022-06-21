# https://oj.leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper_idx = len(nums)
        lower_idx = 0
        idx = (upper_idx-lower_idx)//2
        prev_idx = -1
        while (1):
            if idx == prev_idx:
                return -1
            elif target > nums[idx]:
                lower_idx = idx
            elif target < nums[idx]:
                upper_idx = idx
            else:
                return idx
            prev_idx = idx
            idx = (upper_idx-lower_idx)//2 + lower_idx
                    