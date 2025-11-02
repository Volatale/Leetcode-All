# 69. Sqrt(x)

# * As we observed from the O(sqrt(x)) version of the function, the integers are monotonically increasing
# * Once we hit a square > x, we know that all of the future squares will also be invalid
# ! Thus, given `i`, we can perform (i * i) and determine whether this is a potential return candidate or not
# * The range of possible return values is in the range [1, x]
# * Therefore we have a sorted search space (the range of potential integers)
# ! And this is an optimization problem (we are trying to find something specific given multiple candidates)
# * A binary search approach is possible based on the above observations
# * If (mid * mid) > x, we set right = mid
# *     - Why? Because the return value is always the value 1 before `left`
# * We want to round the result down to the nearest integer
# * So the easiest thing to do is consistently overshoot, and then subtract 1 to get to the correct value
# * If we don't overshoot by 1, then it becomes more difficult to handle the edge cases at the end
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        # * The search space is the range of integer in the range [1, x]
        left: int = 1
        right: int = x

        while left < right:
            # * `mid` represents our current square root candidate
            mid: int = left + ((right - left) >> 1)

            if mid * mid > x:
                right = mid  # * Potential valid candidate found
            else:
                left = mid + 1  # * Square is too small

        # * `left` is always 1 greater than we need it to be
        return left - 1


sol: Solution = Solution()
print(sol.mySqrt(0))  # * 0
print(sol.mySqrt(1))  # * 1
print(sol.mySqrt(2))  # * 2
print(sol.mySqrt(3))  # * 1
print(sol.mySqrt(4))  # * 2
print(sol.mySqrt(5))  # * 2
print(sol.mySqrt(6))  # * 2
print(sol.mySqrt(7))  # * 2
print(sol.mySqrt(8))  # * 2
print(sol.mySqrt(9))  # * 3
print(sol.mySqrt(10))  # * 3

# * Time: O(log n) - We halve the search space within each iteration

# * Space: O(1) - The memory usage remains constant regardless of input size
