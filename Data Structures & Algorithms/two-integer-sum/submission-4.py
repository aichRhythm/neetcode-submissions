class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #define a hash
        #iterate through the array
        #idea is to find whether a complement of the number is already present in the hash
        #if not, add it to the hash

        s = {}

        for i, n in enumerate(nums):

            comp = target - n

            if comp in s:

                return [s[comp], i]

            s[n] = i

        