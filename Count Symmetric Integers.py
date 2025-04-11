# Link: https://leetcode.com/problems/count-symmetric-integers/

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0
        
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                left_sum = sum(int(d) for d in s[:mid])
                right_sum = sum(int(d) for d in s[mid:])
                if left_sum == right_sum:
                    count += 1
        
        return count