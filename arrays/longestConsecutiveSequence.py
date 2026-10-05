class Solution:
    def longestConsecutiveSequence(self, nums: List[int]) -> int:

        # all unique numbers
        numsSet = set(nums)
        longest = 0

        for n in nums:
            # start of sequence
            if n - 1 not in numsSet:
                currentSeq = 0
                while (n + currentSeq) in numsSet:
                    currentSeq += 1
                    longest = max(longest, currentSeq)
        return longest


s = Solution()
print(s.longestConsecutiveSequence([2, 20, 4, 10, 3, 4, 5]))
