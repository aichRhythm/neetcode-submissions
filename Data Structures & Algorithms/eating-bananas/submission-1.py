import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def valid_k(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours <= h
        
        l = 1
        r = max(piles)

        while l < r:
            mid = (r + l) // 2

            if valid_k(mid):
                r = mid

            else:
                l = mid + 1

        return r

