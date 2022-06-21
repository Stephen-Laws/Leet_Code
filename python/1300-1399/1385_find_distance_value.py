# https://oj.leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # sliding pointer after sorting lists



        #Brute force method
        # distance = len(arr1)
        # for i in arr1:
        #     for j in arr2:
        #         if abs(i-j) <= d:
        #             distance -= 1 
        #             break
        # return distance