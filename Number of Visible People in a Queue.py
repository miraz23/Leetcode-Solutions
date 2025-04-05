# Link: https://leetcode.com/problems/number-of-visible-people-in-a-queue/

class Solution(object):
    def canSeePersonsCount(self, heights):
        n = len(heights)
        res = [0] * n
        stack = []

        for i in reversed(range(n)):
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            if stack:
                count += 1
            res[i] = count
            stack.append(heights[i])

        return res