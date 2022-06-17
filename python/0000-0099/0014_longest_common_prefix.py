# https://oj.leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = min(strs,key = len)
        output = ""
        for i, char in enumerate(shortest_str):
            for string in strs:
                if (string[i] != char):
                    return output
            output += char
                
        return output 