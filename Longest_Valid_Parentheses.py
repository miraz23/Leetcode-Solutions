# Link: https://leetcode.com/problems/longest-valid-parentheses/

class Solution(object):
    def longestValidParentheses(self, s):
        res, left, right = 0, 0, 0

        for c in s:
            left += (c == '(')
            right += (c == ')')

            if left == right:
                res = max(res, 2 * right)
            elif right > left:
                left = right = 0

        left = right = 0

        for c in reversed(s):
            left += (c == '(')
            right += (c == ')')
            if left == right:
                res = max(res, 2 * left)
            elif left > right:
                left = right = 0

        return res