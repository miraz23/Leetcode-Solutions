import heapq

class Solution(object):
    def minOperations(self, nums, k):
        minheap = []
        for num in nums:
            heapq.heappush(minheap, num)

        count = 0
        while minheap:
            min1 = heapq.heappop(minheap)
            if min1 >= k:
                break
            min2 = heapq.heappop(minheap)
            heapq.heappush(minheap, 2 * min(min1, min2) + max(min1, min2))
            count += 1
        return count
