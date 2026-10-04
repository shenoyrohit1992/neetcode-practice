from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)  # key: sorted str, val = []

        for s in strs:
            arranged = "".join(sorted(s))
            anagramMap[arranged].append(s)

        return list(anagramMap.values())


s = Solution()
print(s.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
