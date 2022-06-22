# https://oj.leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = self.hash(nums1, nums2)
        return ans

    def hash(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.hash(nums2,nums1)

        
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans

    def sort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        idx1 = 0
        idx2 = 0
        ans = []
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                ans.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
            else:
                idx1 +=1
        return ans