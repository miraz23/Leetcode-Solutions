# Link: https://leetcode.com/problems/longest-nice-subarray/

class Solution(object):
    def longestNiceSubarray(self, nums):
        left = 0
        current = 0
        max_len = 0

        for right in range(len(nums)):
            while (current & nums[right]) != 0:
                current ^= nums[left]
                left += 1

            current |= nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len