# Link: https://leetcode.com/problems/text-justification/

class Solution(object):
    def fullJustify(self, words, maxWidth):
        res, line, ll = [], [], 0

        for word in words:
            if ll + len(line) + len(word) > maxWidth:
                for i in range(maxWidth - ll):
                    line[i % (len(line) - 1 or 1)] += ' '

                res.append(''.join(line))
                line, ll = [], 0 

            line.append(word)
            ll += len(word)

        res.append(' '.join(line).ljust(maxWidth))

        return res