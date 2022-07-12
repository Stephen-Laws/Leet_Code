# https://oj.leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        keys = {}
        for i,char in enumerate(s):
            if char in keys: 
                if t[i] != keys[char]:
                    return False

            else:
                if t[i] in keys.values():
                    return False
                keys[char] = t[i]
        return True