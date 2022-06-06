class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
        keys = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D": 500, "M": 1000}
        special_vals = [1,10,100]
        val = 0
        len_s = len(s)
        for i, char in enumerate(s):
            curr_val = keys[char]
            if curr_val in special_vals:
                if i < len_s-1:
                    next_val = keys[s[i+1]]
                    if curr_val < next_val:
                        val -= curr_val
                    else:
                        val += curr_val
                else:
                    val += curr_val
            else:
                val += curr_val
            
        return val