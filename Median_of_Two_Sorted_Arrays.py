# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        res = []
        for i in range(len(nums1)):
            res.append(nums1[i])
        for i in range(len(nums2)):
            res.append(nums2[i])
        res.sort()
        n = len(res)
        
        if n % 2 == 1:
            return float(res[n // 2])
        else:
            return (res[n // 2 - 1] + res[n // 2]) / 2.0