# 32. Longest Valid Parentheses

# * Since this is a parentheses problem, we can use a stack
# * Every "(" we find is potentially the start of a valid substring
# * When we encounter a ")", naturally, we want to pair this with the most recent "("
# *     - Thus, we pop when we find one
# * To find the length of a valid substring, we use "i - stack[-1]"
# ! If the stack is empty post-pop, that means the stack will lead to invalid substrings
# *     - Therefore, we have to create a new "base index"
# *     - Push the current index to the stack
# ! In the event that the entire string is valid "((()))", we utilize the base index


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # * An empty input cannot have any valid parentheses
        if len(s) == 0:
            return 0

        # * Tracks indices of potential starting points ("(")
        stack: list[int] = [-1]
        max_len: int = 0

        for i, ch in enumerate(s):
            if ch == "(":
                # * Found new potential starting point
                stack.append(i)
            else:
                # * Match the ")" with the top "("
                stack.pop()

                if not stack:
                    # ! This is our new starting point (anything before this is invalid)
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

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

# * Space: O(n) - In the worst case, the stack's size scales linearly with the input size
