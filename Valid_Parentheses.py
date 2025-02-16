# Link: https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        stack = []
        dict = {  ')' : '(',  '}' : '{',  ']' : '[' }
        for c in s:
            if c in dict:
                if stack and stack[-1] == dict[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False