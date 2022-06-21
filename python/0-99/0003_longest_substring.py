# https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        length = 1
        s_len = len(s)
        unique_str = [s[0]]
        for i in range(1,s_len):
            if s[i] in unique_str:
                repeat_idx = unique_str.index(s[i])
                j = -1
                while j < repeat_idx:
                    unique_str.pop(0)
                    j+=1
            unique_str.append(s[i])
            
            if len(unique_str) > length:
                length = len(unique_str)
            
        return length                 
        