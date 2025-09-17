# 22. Generate Parentheses

# * Given `n` pairs of parentheses, the goal is to return all combinations of well-formed parentheses
# *     - In other words, each of the parentheses generated must be VALID
# * In this casem a "well-formed parentheses" is denoted by AB
# * Here is what we know a valid parentheses to be:
# *     - AB is valid: ()
# *     - (AB) is also valid: (())
# *     - As is ABAB: ()()
# ! `n` denotes the number of opening parentheses, as well as the number of closing parentheses
# ! Since we need to generate ALL possible combinations that follow a constraint, we should use backtracking
# * Once a parentheses is "invalid", it can never become valid
# *     - Therefore, we might as well go back to the drawing board
# *     - In this case, that implies a backtrack (a failed candidate was found)
# * There can never be more closers than openers
# * There should never be more than `n` openers, nor more than `n` closers
# * We can only try a closer if there is an opener that needs to be closed

from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # * Handles empty input case
        if n == 0:
            return []

        results: list[str] = []

        # * Simulates stack frames: (openers, closers, currString)
        stack: deque[tuple[int, int, list[str]]] = deque([(0, 0, [])])

        while stack:
            openers, closers, chars = stack.pop()

            # * Base Case
            if openers + closers == n * 2:
                results.append("".join(chars))

            # * Try adding an opener
            if openers < n:
                stack.append((openers + 1, closers, chars + ["("]))

            # * Try adding a closer
            if closers < openers:
                stack.append((openers, closers + 1, chars + [")"]))

        return results


sol: Solution = Solution()
print(sol.generateParenthesis(0))  # * []
print(sol.generateParenthesis(1))  # * ["()"]
print(sol.generateParenthesis(2))  # * ["(())", "()()"]
print(sol.generateParenthesis(5))

# * Time: O(C(n)) - Technically the time complexity is O(2^n) due to the branching factor (2)
# * However, due to the pruning, we eliminate the majority of the branches that could exist
# * Thus, the true time complexity is O(C(n)), where `C` represents the nth catalan number

# * Space: O(n) - The memory usage scales with the size of the input (n)
