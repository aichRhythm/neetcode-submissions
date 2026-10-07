class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        sletters = {}
        tletters = {}
        for letter in s:
            if letter in sletters:
                sletters[letter] += 1
            else:
                sletters[letter] = 1
        for letter in t:
            if letter in tletters:
                tletters[letter] += 1
            else:
                tletters[letter] = 1
        if sletters == tletters:
            return True
        else:
            return False