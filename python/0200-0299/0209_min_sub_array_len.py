# https://oj.leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        start_idx = 0
        max_len = 0
        curr_len = 0
        for i,el in enumerate(nums):
            #Running tally of current score
            curr_sum += el
            
            if curr_sum >= target:
                #Repeatedly remove starting element from start of sum until not true
                while curr_sum - nums[start_idx] >= target:
                    curr_sum -= nums[start_idx]
                    start_idx += 1
                curr_len = (i-start_idx) + 1
                if curr_len < max_len or max_len == 0:
                    max_len = curr_len
                    
        return max_len
                
                    