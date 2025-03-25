# Link: https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s):
        stack = []
        num = 0
        sign = 1
        result = 0
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-":
                result += sign * num
                num = 0
                sign = 1 if char == '+' else -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()
        
        return result + sign * num