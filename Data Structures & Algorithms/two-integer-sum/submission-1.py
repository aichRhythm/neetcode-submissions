class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create an empty dict
        # loop through the array tracking number and its index
        # find a complement to each integers
        # if it exists in the dict, we return the index of the number
        # add each element to the set
        # haven't found any, return false

        s = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in s:
                return [s[complement], i]

            s[num] = i
        
        return False
        