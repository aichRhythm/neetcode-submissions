class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)
        n = len(nums)

        res, sol = [], []

        def backtrack(i, curr_sum):

            if curr_sum == target:
                res.append(sol[:])
                return

            if curr_sum > target or i == n:
                return

            sol.append(nums[i])
            backtrack(i+1, curr_sum + nums[i])
            sol.pop()
            
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, curr_sum)
            
        
        backtrack(0, 0)

        return res