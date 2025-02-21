# Link: https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        freq = defaultdict(int)

        for i in nums:
            freq[i]+=1

        for key, value in freq.items():
            if value > len(nums)/2:
                return key