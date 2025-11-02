# 69. Sqrt(x)

# * At each `i`, square `i` and check if the product > x
# * If it is, then the square has already been found
class Solution:
    def mySqrt(self, x: int) -> int:
        # * sqrt(0) = 0
        if x == 0:
            return 0

        result: int = 0

        # * Find the root via multiplication
        for i in range(1, x + 1):
            if i * i > x:
                break

            result += 1

        return result


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

# * Time: O(sqrt(x)) - The time taken scales with the square root of the input

# * Space: O(1) - The memory usage remains constant regardless of input size
