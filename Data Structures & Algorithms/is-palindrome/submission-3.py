class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_string = [char.lower() for char in s if char.isalnum()]

        pointer1 = 0

        pointer2 = len(clean_string) - 1

        while pointer1 < pointer2:

            if clean_string[pointer1] != clean_string[pointer2]:
                return False
            pointer1 = pointer1 + 1
            pointer2 = pointer2 - 1

        return True