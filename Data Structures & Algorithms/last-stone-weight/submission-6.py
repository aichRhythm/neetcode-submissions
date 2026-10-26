import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:

            pebble1 = -heapq.heappop(stones)
            pebble2 = -heapq.heappop(stones)

            if pebble1 == pebble2:
                continue

            else:
                heapq.heappush(stones, -abs(pebble1 - pebble2))

        return abs(stones[-1]) if stones else 0




