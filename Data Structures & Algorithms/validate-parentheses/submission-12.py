class Solution:
    def isValid(self, s: str) -> bool:
        
        bmap = {')': '(', '}': '{', ']': '['}

        stack = []

        for i in s:

            if i in bmap:

                if stack and stack[-1] == bmap[i]:

                    stack.pop()

                else:

                    return False

            else:

                stack.append(i)

        return True if not stack else False