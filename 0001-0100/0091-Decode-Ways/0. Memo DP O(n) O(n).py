# 91. Decode Ways

# * A valid symbol can only have one or two digits
# * In the one digit case, we only used ONE character
# *     - So on the next stack frame we start 1 character ahead
# *     - (i + 1)
# * In the two digit case, we used TWO characters
# *     - So on the next stack frame, we start 2 characters ahead
# *     - (i + 2)
# ! Thus, this can be optimized using dynamic programming
# *     - F(n) = F(n - 1) + F(n - 2)
class Solution:
    def numDecodings(self, s: str) -> int:
        def decode(i: int) -> int:
            # * Check for memoized subproblems
            if i in memo:
                return memo[i]

            # * Base Case: Completed decoding
            if i == len(s):
                return 1

            # * Base Case: Can't have leading zeroes
            if s[i] == "0":
                return 0

            ways: int = 0

            # * Case 1: Single character case
            ways += decode(i + 1)

            # * Case 2: Double character case
            if i + 1 < len(s) and s[i] <= "2" and s[i + 1] <= "6":
                ways += decode(i + 2)

            memo[i] = ways
            return ways

        memo: dict[int, int] = {}
        return decode(0)


# * Time: O(n) - At each level of recursion, there are two choices in the worst case
# * However, we memoize overlapping subproblems (and there are `n` unique subproblems)

# * Space: O(n) - The depth of recursion scales with the size of the input
