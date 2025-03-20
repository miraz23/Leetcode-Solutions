# Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for op in operations:
            if "+" in op:
                x += 1
            else:
                x -= 1
        return x