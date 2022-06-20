# https://oj.leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_len = len(arr)
        max_arr = arr[-1]
        missing_ints = max_arr - arr_len
        
        if k > missing_ints:
            return max_arr + k-missing_ints
        
        if arr[0] > k:
            return k
        
        #else binary search
        lo = 0
        hi = arr_len
        idx = (arr_len + lo) // 2
        
        while hi > lo:
            if ((arr[idx] -idx) <= k):
                lo = idx +1
            else:
                hi = idx
            idx = (hi+lo)//2

        return idx +k