from collections import defaultdict

class Solution(object):
    def tupleSameProduct(self, nums):
        freq = defaultdict(int)
        ans=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod=nums[i] * nums[j]
                freq[prod]+=1

        for n in freq.values():
            if n > 1:
                ans += ( n * (n-1) // 2 ) * 8

        return ans
        