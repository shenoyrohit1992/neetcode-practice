from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## Scratch: [30,38,30,36,35,40,28]
        ##          [(0, 30), ()]
        res = [0] * len(temperatures)
        stack = []  # store (ind, temp)

        for ind, temp in enumerate(temperatures):
            # pop till we found larger temp
            while stack and temp > stack[-1][1]:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = ind - stackInd

            stack.append((ind, temp))
        return res


s = Solution()
print(s.dailyTemperatures([30, 38, 30, 36, 35, 40, 28]))
