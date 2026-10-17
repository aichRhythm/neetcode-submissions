class Solution:
    def isValid(self, s: str) -> bool:
        
        # create a hashmap of bracket allocations

        # for each closing bracket that goes into the stack, the opening bracket should already exist

        bracket = {')': '(', '}': '{', ']': '['}

        stack = []

        for i in s:

            if i in bracket:

                if stack and stack[-1] == bracket[i]:

                    stack.pop()
                else:

                    return False
            else:

                stack.append(i)   

        return True if not stack else False


                