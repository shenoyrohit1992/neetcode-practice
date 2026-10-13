class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(position[i], speed[i]) for i in range(len(position))]
        # decreasing order sort
        pairs = sorted(pairs, key=lambda x: x[0], reverse=True)

        stack = []
        # append times, if collision, pop
        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)

            if (
                len(stack) >= 2 and stack[-1] <= stack[-2]
            ):  # collision, pop faster coz now they're slower
                stack.pop()
        return len(stack)


s = Solution()
print(s.carFleet(target=10, position=[1, 4], speed=[3, 2]))
