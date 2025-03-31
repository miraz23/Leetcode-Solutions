# Link: https://leetcode.com/problems/put-marbles-in-bags/

class Solution(object):
    def putMarbles(self, weights, k):
        if k == 1:
            return 0
        
        sums = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        sums.sort()
        
        mini = sum(sums[:k-1])
        maxi = sum(sums[-(k-1):])
        
        return maxi - mini