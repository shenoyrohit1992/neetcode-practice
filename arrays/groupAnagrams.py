from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)  # key: sorted str, val = []

        for s in strs:
            arranged = "".join(sorted(s))
            anagramMap[arranged].append(s)

        return list(anagramMap.values())

    def groupAnagramsOptimized(self, strs: List[str]) -> List[List[str]]:
        anagrapMap = defaultdict(
            list
        )  # key: tuple(list of char counts), val: list of strings

        for s in strs:
            countList = [0] * 26

            for c in s:
                countList[ord(c) - ord("a")] += 1

            anagrapMap[tuple(countList)].append(s)
        return anagrapMap.values()


s = Solution()
print(s.groupAnagramsOptimized(["act", "pots", "tops", "cat", "stop", "hat"]))
