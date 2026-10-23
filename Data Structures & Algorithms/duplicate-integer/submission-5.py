class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        s = {}

        for i in nums:

            if i not in s:

                s[i] = 1

            elif s[i] == 1:

                return True

            else:

                s[i] = s[i] + 1
            
        return False

