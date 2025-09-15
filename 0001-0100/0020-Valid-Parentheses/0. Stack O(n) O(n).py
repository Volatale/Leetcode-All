# 20. Valid Parentheses

# * We are given a string `s` and the goal is to determine if it is "valid"
# * A valid input meets the following criteria:
# *      Open brackets must be closed by the same type of bracket
# *      Open brackets must be closed in the correct order
# *      Every close bracket has a corresponding open bracket of the same type
# * So in other words
# *     - Openers can only be closed by closers of the same type
# *     - We can't have more closers than openers
# *     - Every opener must be be closed
# *     - The order matters
# ! Ultimately, this is a LIFO problem, so we should use a stack data structure
# * When we encounter an opener, we push the corresponding closer to the stack
# * If the top of the stack does not equal the current closer s[i], then the input was invalid
class Solution:
    def isValid(self, s: str) -> bool:
        # * The stack gives us fast access to whatever closer we need
        stack: list[str] = []

        for char in s:
            match char:
                case "(":
                    stack.append(")")
                case "[":
                    stack.append("]")
                case "{":
                    stack.append("}")
                case _:
                    if not stack or char != stack.pop():
                        return False

        # * The stack must also be empty for the input to be valid
        return len(stack) == 0


sol: Solution = Solution()
print(sol.isValid("()"))  # * True
print(sol.isValid("()[]{}"))  # * True
print(sol.isValid("(}"))  # * False
print(sol.isValid("([])"))  # * True
print(sol.isValid("([)]"))  # * False
print(sol.isValid("{}"))  # * True

# * Time: O(n) - The time taken scales with the length of the input

# * Space: O(n) - In the worst case, we nevr pop anything from the stack
# * For example, with "((((", the size of the stack is equal to the input length (n)
