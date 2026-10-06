class Solution:
    def containsMaxArea(self, heights: List[int]) -> int:
        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r:
            currentArea = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, currentArea)

            if heights[r] < heights[l]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1

        return maxArea
