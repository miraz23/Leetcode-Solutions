# Link: https://leetcode.com/problems/valid-number/

class Solution(object):
    def isNumber(self, s):
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        return bool(re.match(pattern, s.strip()))