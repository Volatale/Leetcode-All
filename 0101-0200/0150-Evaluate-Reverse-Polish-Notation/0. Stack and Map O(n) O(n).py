# 150. Evaluate Reverse Polish Notation

# * The easiest thing to do is use a stack
# * Note that the elements are processed in reverse order
# * If we find an operator (+, -, *, /), then we pop the top two elements from the stack
# * Otherwise, push the operand to the stack

# * Division truncates toward 0
# * No division by 0
# * Mathematically, there are two operands for every operator
# *     - Thus, regarding branch prediction, it is more likely that we find an operator
# * In terms of scalability, it makes sense to use a dictionary since it allows for future-proofing
# *     - It is also more readable than just using a switch statement
from collections.abc import Callable
from math import trunc


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # * A dictionary of functions prevents the need for a switch
        operations: dict[str, Callable[[int, int], int]] = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: trunc(a / b),
        }

        # * RPN process nodes in LIFO order, so we need a stack
        operands: list[int] = []

        for token in tokens:
            if token not in operations:
                operands.append(int(token))
            else:
                num2: int = int(operands.pop())
                num1: int = int(operands.pop())
                operands.append(operations[token](num1, num2))

        return operands[0]


# * Time: O(n) - We have to process every element in the input list

# * Space: O(n) - There are 2n operands for every operator, so the memory usage scales with input size
