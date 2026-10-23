class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        shash = {}

        thash = {}

        if len(s) != len(t):

            return False

        for i in s:

            if i not in shash:

                shash[i] = 0

            else:

                shash[i] = shash[i] + 1

        for j in t:

            if j not in thash:

                thash[j] = 0

            else:

                thash[j] = thash[j] + 1

        return shash == thash

            