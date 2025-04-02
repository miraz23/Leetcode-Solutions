# Link: https://leetcode.com/problems/special-binary-string/

class Solution(object):
    def makeLargestSpecial(self, s):
        if not s:
            return ""

        res = []
        a, b = 0, 0
        for i, char in enumerate(s):
            a += 1 if char == '1' else -1
            if a == 0:
                inner = self.makeLargestSpecial(s[b + 1:i])
                res.append('1' + inner + '0')
                b = i + 1
        return ''.join(sorted(res, reverse=True))