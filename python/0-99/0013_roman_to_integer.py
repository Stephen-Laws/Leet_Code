# https://oj.leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
        keys = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D": 500, "M": 1000}
        val = 0 
        for i in range(len(s) - 1):
            if keys[s[i]] < keys[s[i+1]]:
                val -= keys[s[i]]
            else:
                val += keys[s[i]]
           
        return val + keys[s[i-1]]