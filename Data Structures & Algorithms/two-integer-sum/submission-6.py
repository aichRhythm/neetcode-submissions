class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        s = {}

        for i, v in enumerate(nums):

            comp = target - v

            if comp in s:

                return [s[comp], i]

            else:

                s[v] = i