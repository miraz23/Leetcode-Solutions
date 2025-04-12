# Link: https://leetcode.com/problems/number-of-good-pairs/

class Solution(object):
    def numIdenticalPairs(self, nums):
        count = defaultdict(int)
        good_pairs = 0

        for num in nums:
            good_pairs += count[num]
            count[num] += 1

        return good_pairs