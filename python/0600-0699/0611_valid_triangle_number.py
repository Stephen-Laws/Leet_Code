<<<<<<< HEAD
# https://oj.leetcode.com/problems/valid-triangle-number/
=======
# https://oj.leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums):
        nums, count, n = sorted(nums), 0, len(nums)
        for i in range(2, n):
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        return count
>>>>>>> 94195ef0390b1becebf16f32c375d9968d8eb497
