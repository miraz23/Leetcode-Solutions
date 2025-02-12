#Link: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

'''
# Wrong answer-
# Input: nums = [368,369,307,304,384,138,90,279,35,396,114,328,251,364,300,191,438,467,183]
# Output: 765
# Expected: 835

class Solution:
    def maximumSum(self, nums):
        max_sum = -1
        sum_map = {}

        for i in range(len(nums)):
            a = nums[i] % 10
            b = nums[i] / 10
            sum = a+b

            if sum in sum_map:
                max_sum = max(max_sum, sum_map[sum] + nums[i])
                sum_map[sum] = max(sum_map[sum], nums[i])
            else:
                sum_map[sum] = nums[i]

        return max_sum
'''

#Accepted

class Solution:
    def maximumSum(self, nums):
        max_sum = -1
        sum_map = {}

        for i in range(len(nums)):
            sum = 0
            temp = nums[i]
            while temp:
                sum += temp % 10
                temp /= 10

            if sum in sum_map:
                max_sum = max(max_sum, sum_map[sum] + nums[i])
                sum_map[sum] = max(sum_map[sum], nums[i])
            else:
                sum_map[sum] = nums[i]

        return max_sum