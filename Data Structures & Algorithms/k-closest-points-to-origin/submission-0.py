import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in points:
            dist = (0-i[0])**2 + (0-i[1])**2
            heapq.heappush(heap, [dist, i])
        
        ans = []

        for i in range(k):
            x = heapq.heappop(heap)
            ans.append(x[1])
        
        return ans