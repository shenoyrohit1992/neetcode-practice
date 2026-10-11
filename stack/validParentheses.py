class Solution:
    def isValid(self, s: str) -> bool:

        parenthesisMap = {")": "(", "]": "[", "}": "{"}
        stack = []  # LIFO

        for char in s:
            # open
            if char in parenthesisMap.values():
                stack.append(char)
            # closing
            elif char in parenthesisMap:
                # stack should not be empty
                if stack and stack[-1] == parenthesisMap[char]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False


s = Solution()
print(s.isValid("([{}])"))
print(s.isValid("[[)"))
