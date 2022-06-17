# https://oj.leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        idx = (hi+lo)//2
        while hi > lo:
            if isBadVersion(idx):
                hi = idx
            else:
                lo = idx+1
            idx = (hi+lo)//2
        return idx
                