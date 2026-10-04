class Solution:
    def getTopKElements(self, nums: List[int], target: int) -> List[int]:

        # store counts in hashmap (key: num, val: counts)
        counts = {}
        frequencies = [[] for x in range(len(nums))]

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        # array that stores for every count (at index), a list of nums in original
        for num, count in counts.items():
            frequencies[count].append(num)

        # get top k
        res = []
        for ind in range(len(nums) - 1, 0, -1):
            for num in frequencies[ind]:
                res.append(num)
                if len(res) == target:
                    return res
        return


s = Solution()
print(s.getTopKElements(nums=[1, 2, 2, 3, 3, 3], target=2))
