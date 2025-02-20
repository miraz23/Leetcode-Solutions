# Link: https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        freq = Counter(nums)
        for num, count in freq.items():
            if count == 1:
                return num