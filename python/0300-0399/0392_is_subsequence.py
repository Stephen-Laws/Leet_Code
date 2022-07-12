# https://oj.leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        idx = 0
        for char in t:
            if char == s[idx]:
                idx += 1
                if len(s) == idx:
                    return True
        return False