class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s = {}
        
        for i, j in enumerate(nums):

            comp = target - j

            if comp in s:

                return [s[comp], i]
            
            s[j] = i

            