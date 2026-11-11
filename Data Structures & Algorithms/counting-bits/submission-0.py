class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []

        for i in range(n+1):
            an = 0
            while i != 0:
                i &= i - 1
                an += 1
            ans.append(an)
        
        return ans