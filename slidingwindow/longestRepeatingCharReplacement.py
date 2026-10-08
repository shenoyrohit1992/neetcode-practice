class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        countMap = {}

        l = 0

        for r in range(len(s)):
            countMap[s[r]] = 1 + countMap.get(s[r], 0)

            # invalid window - breaking condition
            while (r - l + 1) - max(countMap.values()) > k:
                countMap[s[l]] = countMap[s[l]] - 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest


s = Solution()
print(s.characterReplacement(s="AAABABB", k=1))
