class Solution:
    def isPalindrome(self, s: str) -> bool:
        #make string alphanumeric
        #initiae the pointers
        #check if left == right
        #if true, go next
        #if false, return false

        cleaned_string = [char.lower() for char in s if char.isalnum()]
        left = 0
        right = len(cleaned_string) - 1

        while left < right:
            if cleaned_string[left] != cleaned_string[right]:
                return False
            left = left + 1
            right = right - 1

        return True
            
