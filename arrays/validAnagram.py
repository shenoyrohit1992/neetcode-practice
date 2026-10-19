class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}  # key: char, val: count
        # optimized = can be two arrays of [0] * 26,
        # and each index holds count of the characters a-z

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)

        return sMap == tMap

    def isAnagramOptimized(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = [0] * 26, [0] * 26

        for i in range(len(s)):
            sMap[ord(s[i]) - ord("a")] += 1
            tMap[ord(t[i]) - ord("a")] += 1

        for ind in range(len(sMap)):
            if sMap[ind] != tMap[ind]:
                return False
        return True


s = Solution()
print(s.isAnagram(s="racecar", t="carrace"))
print(s.isAnagram(s="jar", t="jam"))
