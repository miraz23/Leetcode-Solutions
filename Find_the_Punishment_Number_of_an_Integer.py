# Link: https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution:
    def punishmentNumber(self, n):
        ans = 1
        for i in range(2, n + 1):
            mul = str(i * i)
            if self.isValid(mul, 0, 0, i):
                ans += i * i
        return ans
    
    def isValid(self, mul, pos, sum, val):
        if pos >= len(mul):
            return sum == val
        
        for i in range(len(mul) - pos):
            curr = int(mul[pos:pos + i + 1])
            if self.isValid(mul, pos + i + 1, sum + curr, val):
                return True
        return False