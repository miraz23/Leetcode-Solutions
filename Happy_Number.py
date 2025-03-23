# Link: https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n):
        if n == 1 :
            return True
        if n < 6:
            return False
       
        ans = 0
        for i in str(n):
            ans += int(i)*int(i)
        
        return self.isHappy(ans)