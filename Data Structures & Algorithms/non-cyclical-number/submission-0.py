class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = set()

        while n != 1:
            str_n = str(n)
            n = sum(int(d)**2 for d in str_n)
            if n != 1 and n in s:
                return False
            else:
                s.add(n)
        return True