import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        n = len(stones)

        for i in range(n):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while n > 1:
            n = len(stones)

            if n > 1:
                first = -heapq.heappop(stones)
                second = -heapq.heappop(stones)
            elif n == 1:
                return -stones[0]
            else:
                return 0

            flint = abs(first - second)

            if flint > 0:
                heapq.heappush(stones, -flint)

        return 0 if not stones else -stones[0]
