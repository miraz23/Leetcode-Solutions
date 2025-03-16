# Link: https://leetcode.com/problems/reducing-dishes/

class Solution(object):
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort(reverse=True)
        total, sum = 0, 0

        for s in satisfaction:
            if sum + s > 0:
                sum += s
                total += sum
            else:
                break

        return total