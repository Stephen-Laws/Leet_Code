# https://oj.leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        idx = (r-l)//2
        i = 0
        while r > l+1:
            if arr[idx] > arr[idx+1]:
                r = idx
            else:
                l = idx
            idx = (r-l)//2+l
        return r 