import heapq
import copy

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        mh = [-n for n in nums]
        heapq.heapify(mh)
        print(mh)
        self.heap = mh
        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)

        x = copy.deepcopy(self.heap)

        for i in range(self.k):
            possible = heapq.heappop(x)
        
        return -possible

