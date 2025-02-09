from collections import defaultdict

class Solution:
    def countBadPairs(self, nums):
        n = len(nums)
        '''
        for good pair
        i - j == nums[i] - nums[j]
        nums[i] - i == nums[j] - j
        '''
        freq = defaultdict(int)
        good_pairs = 0
        # 0 1 2 3
        # 4 1 3 3
        '''
        K   |   V
        4   |   1
        0   |   1,2 -> good_pairs = 1
        1   |   1   
        '''
        for i in range(n):
            key = nums[i] - i
            if key in freq:
                good_pairs += freq[key]
            freq[key] += 1

        total_pairs = n * (n - 1) / 2 #6
        bad_pairs = total_pairs  - good_pairs #6-1
        return bad_pairs #5