class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sublen = 0
        left = 0
        sett = set()

        for right in range(len(s)):

            while s[right] in sett:
                sett.remove(s[left])
                left += 1

            sublen = max(sublen, right - left + 1)
            sett.add(s[right])
        
        return sublen
