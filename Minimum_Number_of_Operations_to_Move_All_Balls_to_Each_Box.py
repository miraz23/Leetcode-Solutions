# Link: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        result = [0] * n

        for i in range(n):
            count = 0
            for j in range(n):
                if boxes[j] == '1':
                    count += abs(i - j)
            result[i] = count

        return result
        