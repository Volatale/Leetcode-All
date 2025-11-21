# 87. Scramble String

# * If the string's length is 1, we stop (base case)
# * Otherwise, the string's length is > 1, so:
# *     1. Split the string at a random index (s = x + y)
# *     2. Randomly decide to swap the two substrings or to keep them in the same order
# *         Case 1: s = x + y
# *         Case 2: s = y + x
# *     3. Apply step 1 recursively on each of the substrings
# * We have to try splitting the string at each index
# * For example, the string "sonic" could become:
# *     "" "sonic"
# *     "s" "onic"
# *     "so" "nic"
# *     "son" "ic"
# *     "soni" "c"
# *     "sonic" ""
# * So essentially, perform a split at each index `i`
# * Then, for each split, we have two branches:
# *     Case 1: Swap
# *     Case 2: Don't swap
# * Only one of the above cases must return true
# ! We can prune the branches by sorting both inputs at each level
# * The characters in both must be identical, as must the frequencies
# * If one of these is not the case, then they can never become equal
# ! Here are the combinations:
# *     s1 = left1 + right1
# *     s2 = left2 + right2
# * dfs(left1, left2) and dfs(right1, right2)
# * dfs(left1, right2) and dfs(right1, left2)
class Solution:
    def isScramble(self, s1: str, s2: str):
        def dfs(a: str, b: str) -> bool:
            # * Check for memoized subproblem
            if (a, b) in memo:
                return memo[(a, b)]

            # * Base Case: s1 can be scrambled to make s2
            if a == b:
                return True

            # * The characters and frequencies must match in both
            if sorted(a) != sorted(b):
                return False

            n = len(a)

            for i in range(1, n):
                # * Case 1: No Swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True

                # * Case 2: Swap (notice how a is never swapped, only b)
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        if len(s1) != len(s2):
            return False

        memo: dict[tuple[str, str], bool] = {}
        return dfs(s1, s2)


sol: Solution = Solution()
print(sol.isScramble("great", "rgeat"))  # * True
print(sol.isScramble("abcde", "caebd"))  # * False
print(sol.isScramble("a", "a"))  # * True
print(sol.isScramble("ab", "ba"))  # * True

# * Time: O(n^4) - There are n^2 substrings for s1, and n^2 substrings for s2
# * So in the worst case, we end up with n^4 subproblems
# * Sorting allows us to immediately prune redundant branches, so its closer to O(n^3)
# * Additionally, we memoize repeated subproblems (but this has no effect on the complexity)

# * Space: O(n^2) - There are n^2 possible substrings, thus n^2 unique subproblems
