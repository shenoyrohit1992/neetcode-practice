# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the k-th permutation sequence.

# Example 1:
# Input: n = 3, k = 3
# Output: "213"

# Example 2:
# Input: n = 4, k = 9
# Output: "2314"

# Example 3:
# Input: n = 3, k = 1
# Output: "123"


## Clarifying questions / edge cases

## Approach:
## n = 4, k = 9

# factorials of 1 -> n = [1, 1, 2, 6, 24...]
# digits = [1, 2, 3, 4], n = 4
# k = 8 (0 indexed)

# for i in 0...n-1:
# factorialDivisor = (n - i)
# digitIndexToSet = k // factorial[factorialDivisor - 1]
# append to result; pop digits[digitToSet]
# k = k % factorial[factorialDivisor - 1]

# n=4, k=9
# fact = [1, 1, 2, 6, 24]
# digits = [1, 2, 3, 4]
# k = 8

# i=0: m=4, fact[3]=6
#   q = 8 / 6 = 1, k = 8 % 6 = 2
#   digits.pop(1) → 2; digits = [1, 3, 4]
#   result = "2"

# i=1: m=3, fact[2]=2
#   q = 2 / 2 = 1, k = 2 % 2 = 0
#   digits.pop(1) → 3; digits = [1, 4]
#   result = "23"

# i=2: m=2, fact[1]=1
#   q = 0 / 1 = 0, k = 0 % 1 = 0
#   digits.pop(0) → 1; digits = [4]
#   result = "231"

# i=3: m=1, fact[0]=1
#   q = 0 / 1 = 0
#   digits.pop(0) → 4
#   result = "2314"

# Return "2314"


class Solution:
    def kThPermutationOfN(self, n: int, k: int) -> str:
        fact = [1] * (n + 1)
        result = ""

        # Pre-computed factorials: [1, 1, 2, 6, 24, ..]
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        digits = list(range(1, n + 1))  # [1, 2, 3, 4]
        k -= 1  # 0-indexed

        for i in range(n):
            factorialDivisorIndex = n - i
            q = k // fact[factorialDivisorIndex - 1]
            digitToSet = digits[q]
            digits.pop(q)
            result += str(digitToSet)
            k = k % fact[factorialDivisorIndex - 1]
        return result


s = Solution()
print(s.kThPermutationOfN(n=4, k=9))
