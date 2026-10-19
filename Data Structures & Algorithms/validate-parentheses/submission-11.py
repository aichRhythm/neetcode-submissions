class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_book = {')': '(', '}': '{', ']': '['}

        stack = []

        for i in s:

            if i in bracket_book:

                if stack and stack[-1] == bracket_book[i]:

                    stack.pop()
                
                else:

                    return False

            else:
                
                stack.append(i)

        return True if not stack else False
                
