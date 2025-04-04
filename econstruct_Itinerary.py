# Link: https://leetcode.com/problems/reconstruct-itinerary/

class Solution(object):
    def findItinerary(self, tickets):
        dic = defaultdict(list)

        for i, j in tickets:
            heapq.heappush(dic[i], j)

        res = []

        def visit(n):
            while dic[n]:
                next_dest = heapq.heappop(dic[n])
                visit(next_dest)
            res.append(n)

        visit("JFK")
        return res[::-1]