class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res, sol = [], []

        def backtrack():

            if len(sol) == n:
                res.append(sol[:])
                return

            for item in nums:
                if item not in sol:
                    sol.append(item)
                    backtrack()
                    sol.pop()
        backtrack()
        return res
