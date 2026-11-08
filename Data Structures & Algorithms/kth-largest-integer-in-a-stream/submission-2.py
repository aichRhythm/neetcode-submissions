import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.numHeap, self.k = nums, k

        heapq.heapify(self.numHeap)

        while len(self.numHeap) > self.k:
            heapq.heappop(self.numHeap)
        

    def add(self, val: int) -> int:

        heapq.heappush(self.numHeap, val)

        if len(self.numHeap) > self.k:
            heapq.heappop(self.numHeap)

        return self.numHeap[0]
        
