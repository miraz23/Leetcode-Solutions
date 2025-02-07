from collections import defaultdict

class Solution(object):
    def queryResults(self, limit, queries):
        color_freq = defaultdict(int)
        ball_color = {}
        result = []

        for i in range(limit):
            ball, color = queries[i]

            if ball in ball_color:
                color_freq[ ball_color[ball] ] -= 1

                if color_freq[ ball_color[ball] ] == 0:
                    del color_freq[ ball_color[ball] ]

            ball_color[ball] = color
            color_freq[color] += 1

            result.append(len(color_freq))

        return result
        