# Link: https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        flowers = sorted(zip(growTime, plantTime), reverse=True)

        count = 0
        ans = 0

        for g, p in flowers:
            count += p
            ans = max(ans, count + g)

        return ans