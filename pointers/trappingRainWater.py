class Solution:
    def trap(self, height: List[int]) -> int:

        waterArea = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                waterArea += maxL - height[l]
            elif maxR <= maxL:
                r -= 1
                maxR = max(maxR, height[r])
                waterArea += maxR - height[r]
        return waterArea
