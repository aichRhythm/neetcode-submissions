class Solution:
    def isValid(self, s: str) -> bool:
        
        # bracket_map = {')': '(', '}': '{', ']': '['}

        # stack = []

        # for c in stack:

        #     if c in bracket_map:

        #         if stack and stack[-1] == bracket_map[c]:

        #             stack.pop()
        #         else:

        #             return False
        #     else:
        #         stack.append(c)
            
        # return True if not stack else False

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
