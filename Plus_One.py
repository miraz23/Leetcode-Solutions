# Link: https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        string = ""
        ans = []
        for i in digits:
            string += str(i)
        
        digit = int(string) + 1
        
        for i in str(digit):
            ans.append(int(i))

        return ans