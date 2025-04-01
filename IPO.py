# Link: https://leetcode.com/problems/ipo/

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
    
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            if not max_heap:
                break

            w += -heapq.heappop(max_heap)
        
        return w