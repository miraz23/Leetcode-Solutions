# Link: https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        res = reduce(math.gcd, nums)
        return res == 1