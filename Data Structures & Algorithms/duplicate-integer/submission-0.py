class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = []
        for instance in nums:
            if instance in items:
                return True
            else:
                items.append(instance)
        return False