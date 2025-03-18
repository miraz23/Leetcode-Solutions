# Link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution(object):
    def findWinners(self, matches):
        losses = defaultdict(int)
        
        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            losses[loser] += 1

        zero = [player for player in losses if losses[player] == 0]
        one = [player for player in losses if losses[player] == 1]
        
        return [sorted(zero), sorted(one)]