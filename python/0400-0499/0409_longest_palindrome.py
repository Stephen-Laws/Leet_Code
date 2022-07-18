# https://oj.leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = [0]*128
        for c in s:
            freq[ord(c)] += 1
        odds = 0
        for i in freq:
            if i > 0:
                print(i, i&1)
            odds += i & 1
        return len(s) - odds + (odds > 0)
            