# https://oj.leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        max_len = 0
        l1, l2 = len(nums1), len(nums2)
        while i < l1 and j < l2:
            if nums1[i] <= nums2[j]:
                if j - i > max_len:
                    max_len = j - i
                j += 1
            elif j != i:
                i +=1
            else:  
                j += 1
        return max_len 