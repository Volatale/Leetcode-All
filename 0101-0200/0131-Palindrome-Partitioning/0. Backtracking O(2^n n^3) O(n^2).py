# 131. Palindrome Partition

# * For each substring in `s`, and for each index `i` within that substring
# * We can make the choice to split, or not to split
# *     - Thus, we have two choices to make
# * It is possible to check for the existence of a palindrome in O(n)
# * Since we want EVERY possible palindrome partitioning, we are using backtracking
# *     - This lets us explore a path in its entirety, while still being able to try every possibility
# * Additionally, since not every substring is a palindrome, we effectively prune most paths
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def backtrack(start: int, path: list[str]):
            # * Base Case: Used all characters
            if start == len(s):
                results.append(path[:])
                return

            # * Try every substring from the current level
            for i in range(start, len(s)):
                ss: str = s[start : i + 1]

                # * Validate candidate
                if is_palindrome(ss):
                    path.append(ss)  # * Choose candidate
                    backtrack(i + 1, path)  # * Explore branch
                    path.pop()  # * Unchoose candidate

        def is_palindrome(s: str) -> bool:
            # * An empty string is a palindrome
            if s == "" or len(s) == 1:
                return True

            n: int = len(s)

            for i in range(n >> 1):
                if s[i] != s[n - 1 - i]:
                    return False

            return True

        results: list[list[str]] = []
        backtrack(0, [])
        return results


sol: Solution = Solution()
print(sol.partition("aab"))  # * [["a", "a", "b"], ["aa", "b"]]
print(sol.partition("a"))  # * [["a"]]
print(sol.partition("abc"))  # * [["a", "b", "c"]]

# * Time: O(2^n + n^3) - We have two choices at each level of recursion
# * Additionally, within each level of recursion, we have an O(n) loop
# * Then, within that loop, it takes O(n) in the worst case to generate a substring
# * And on top of that, it takes O(n) to validate the palindrome-ness of that substring
# * That gives us O(2^n + n^3) in the absolute worst case

# * Space: O(n^2) - If we have a string like "aaaaa", every substring is a substring
# * And all of these substrings are included in the resulting array
