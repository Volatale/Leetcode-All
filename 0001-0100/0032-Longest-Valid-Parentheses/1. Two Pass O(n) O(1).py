# 32. Longest Valid Parentheses

# * Instead of using a stack to handle the `openers` and `closers` we can track the counts manually
# *     - If we find an "(", increment the number of `openers`
# *     - Otherwise, we found an ")", so increment the number of `closers`
# ! We know we have a valid substring when `openers` == `closers`
# * If that is NOT the case, and we are going from left to right
# * Then we likely have more `closers` than `openers`
# ! In that case, we need to reset the counts of both `openers` and `closers`
# *     - Why? Because whatever substring we currently have is invalid
# *     - And as such, we can't include it in a valid substring (because it will NEVER become valid)
# ! However, we need to do the same checks in the reverse direction
# * Imagine we have an input like "(()"
# *     - By the time we are at index 2, we have `openers = 2` and `closers = 1`
# * Since openers != closers, we never actually count "()" as valid
# * But if we iterate in reverse, we'll see that "()" DOES in fact get counted
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # * An empty input cannot have any valid parentheses
        if len(s) == 0:
            return 0

        max_len: int = 0

        # * Track the no. of openers and closers we have
        openers: int = 0
        closers: int = 0

        # * Find the valid substrings going from left to right
        for ch in s:
            if ch == "(":
                openers += 1
            else:
                closers += 1

            if openers == closers:
                max_len = max(max_len, closers * 2)
            elif closers > openers:
                openers = 0
                closers = 0

        openers = 0
        closers = 0

        # * Find the valid substrings going from right to left
        for ch in reversed(s):
            if ch == "(":
                openers += 1
            else:
                closers += 1

            if openers == closers:
                max_len = max(max_len, closers * 2)
            elif openers > closers:
                openers = 0
                closers = 0

        return max_len


sol: Solution = Solution()
print(sol.longestValidParentheses("))()"))  # * 2
print(sol.longestValidParentheses("(()"))  # * 2
print(sol.longestValidParentheses(")()())"))  # * 4
print(sol.longestValidParentheses(""))  # * 0
print(sol.longestValidParentheses("((()))"))  # * 6
print(sol.longestValidParentheses("))()(())"))  # * 6
print(sol.longestValidParentheses("))()))"))  # * 2
print(sol.longestValidParentheses(")("))  # * 0
print(sol.longestValidParentheses(")"))  # * 0
print(sol.longestValidParentheses("("))  # * 0

# * Time: O(n) - The tiem taken scales with the size of the input

# * Space: O(1) - The memory usage remains constant regardless of input size
