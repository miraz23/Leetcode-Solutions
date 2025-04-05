# Link: https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

class Solution(object):
    def shortestSequence(self, rolls, k):
        s = set()
        count = 0
        for i in rolls:
            s.add(i)
            if len(s) == k:
                count += 1
                s.clear()
        return count + 1