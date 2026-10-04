class Solution:
    def checkTwoSum(self, nums: List[int], target: int) -> bool:
        prevMap = {}  # key: num, val: index

        for ind, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], ind]
            prevMap[num] = ind
        return


s = Solution()
print(s.checkTwoSum([3, 1, 5, 4, -2, 6], 7))
