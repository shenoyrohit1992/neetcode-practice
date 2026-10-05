class Solution:
    def isPalindrome(self, s: str) -> bool:
        # inline helper
        def isAlphanumeric(c: str) -> bool:
            if (
                ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
            ):
                return True
            return False

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isAlphanumeric(s[l]):
                l += 1
            while r > l and not isAlphanumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True


s = Solution()
print(s.isPalindrome("Was it a car or a cat I saw?"))
print(s.isPalindrome("tab a cat"))
