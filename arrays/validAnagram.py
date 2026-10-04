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


s = Solution()
print(s.isAnagram(s="racecar", t="carrace"))
print(s.isAnagram(s="jar", t="jam"))
