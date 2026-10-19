class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        shash = {}

        thash = {}

        for i in s:

            if i in shash:

                shash[i] = shash[i] + 1

            else:

                shash[i] = 0
        
        for j in t:

            if j in thash:

                thash[j] = thash[j] + 1

            else:

                thash[j] = 0

        return shash == thash