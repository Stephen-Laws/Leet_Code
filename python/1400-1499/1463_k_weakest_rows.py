# https://oj.leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = [sum(x) for x in mat]
        sorted_strength = [i[0] for i in sorted(enumerate(strength), key=lambda x:x[1])]
        return sorted_strength[:k]
        