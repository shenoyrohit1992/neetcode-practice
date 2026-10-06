class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for ind, num in enumerate(nums):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue

            # new number + two sum
            l, r = ind + 1, len(nums) - 1

            while l < r:
                currSum = num + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                elif currSum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
