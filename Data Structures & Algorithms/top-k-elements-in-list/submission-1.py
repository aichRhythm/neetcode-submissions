import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        stk = {}

        for i in nums:
            if i not in stk:
                stk[i] = 0
            else:
                stk[i] = stk[i] + 1
        
        heap = []
        for num in stk:
            heapq.heappush(heap, (stk[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        print(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res