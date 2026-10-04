class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left, right, output = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        # left stores every val to left of current num, same for right
        prodL, prodR = 1, 1

        for i in range(len(nums)):
            left[i] = left[i] * prodL
            prodL = prodL * nums[i]
        # [1, 1, 2, 8]

        for j in range(len(nums) - 1, -1, -1):
            right[j] = right[j] * prodR
            prodR = prodR * nums[j]
        # [48 24 6 1]

        for k in range(len(nums)):
            output[k] = left[k] * right[k]

        return output


s = Solution()
print(s.productExceptSelf([1, 2, 4, 6]))
print(s.productExceptSelf([-1, 0, 1, 2, 3]))
