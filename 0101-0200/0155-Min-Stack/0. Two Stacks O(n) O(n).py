# 155. Min Stack

# ! Every time you find a new minimum, we need a way to retrieve what the PREVIOUS minimum was
# * One thought process you can take is to manually track the sequence of minimums
# * For [5, 6, 1, 3, 2, 0], the sequence goes:
# *     INF -> 5 -> 1 -> 0
# * Thus, when popping, the sequence must go in reverse (which hints to a LIFO order)
# *     0 -> 1 -> 5 -> INF
# * Otherwise we'll lose track of the series of minimums at some point
# * The easiest thing to do is to use two separate stacks
# *     - The first stack just acts as a regular stack
# *     - The second is stack provides O(1) access to the minimum element in the stack
# * Whenever we need to process a new element, we need to determine what to do:
# * For each `x` we want to push:
# *     - If `x` < the current minimum, we have a new minimum -> push `x` to the min stack
# *         - This ensures that we have O(1) access to the minimum element without it being ontop of `stack`
# *     - Next, push `x` onto the regular stack
# * For each element `x` we want to pop:
# *     - If x == min_stack[-1], pop min_stack
# *     - Then, simply pop the top element of stack


class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = [(1 << 31) - 1]

    def push(self, val: int) -> None:
        # * We have a new minimum; push duplicates too for cases like [1, 3, 1]
        if val <= self.min_stack[-1]:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        # * If true, our "min" becomes the previous min
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# *  0  1  2  3  4  5  6  7
# * [5, 6, 3, 1, 9, 5, 6, 1]
# *                       i

# * min = inf -> 5 -> 3 -> 1
# * stack = [5, 6, 3, 1, 9, 5, 6, ]
# * min_stack = [inf, 5, 3, 1, 1]
