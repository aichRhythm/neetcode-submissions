from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)

        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c) - ord('a')] += 1

            key = tuple(arr)
            group_anagrams[key].append(s)

        return list(group_anagrams.values())
