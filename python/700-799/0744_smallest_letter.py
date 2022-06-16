class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        lo= 0
        hi = len(letters)-1
        idx = (hi+lo) //2
        while hi > lo:
            if letters[idx] > target:
                hi = idx
            else:
                lo = idx + 1
            idx = (hi+lo)//2

        return letters[idx]