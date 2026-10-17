class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # identify middle of array
        # if middle is target return index of target
        # if middle is larger than target, move middle to left
        # if middle is smaller than target, move mjmidddle to right
        # [1,2,3,4,5]

        lo = 0

        hi = len(nums) - 1

        while lo <= hi:

            middle = lo + (hi - lo) // 2

            if nums[middle] == target:

                return middle
            
            elif nums[middle] < target:

                lo = middle + 1

            else:
                
                hi = middle - 1

        return -1