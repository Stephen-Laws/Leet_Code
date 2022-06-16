# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        upper = n
        lower = 1
        guess_val = (upper+lower) //2 
        while upper > lower:
            if guess(guess_val) == 1:
                lower = guess_val+1
            else:
                upper = guess_val
            guess_val = (upper+lower) //2
        return guess_val
        