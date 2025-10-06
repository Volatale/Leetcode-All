# 42. Trapping Rain Water

# * The biggest observation we need to make is that the water trappable at `i` depends on the left and right walls
# *     - Precompute the maximum value from left to right for each wall (starting at index 1)
# *     - Do the same for the values from right to left (starting at index n - 2)
# ! The amount of water trappable at index `i` is bottlenecked by the minimum of the walls to our left and right
# * For example, imagine we have [4, 1, 3]
# *     - At index 1, the largest wall to our left is 4
# *       And the largest wall to our right is 3
# *         - The minimum of the to is: min(4, 3) = 3
# * To get the amount of water at index 1, we do:
# *     - max(0, min(LtoR[i], RtoL[i]) - height[i])
# *     - We subtract height[i] because this removes the "wall" itself from the calculation (thus we are left with just the water)
# ! Why take the maximum of 0 and the result of the computation?
# *     - Because the minimum amount of water that can be trapped at ANY index is 0
# *     - That is to say, we can't store a negative amount of water, so the minimum would have to be 0


class Solution:
    def trap(self, height: list[int]) -> int:
        n: int = len(height)

        if n == 0:
            return 0

        LtoR: list[int] = [0] * n  # * Tallest wall on the left of index `i`
        RtoL: list[int] = [0] * n  # * Tallest wall on the right of index `i`
        water: int = 0

        # * Precompute the tallest walls to the left and to the right of `i`
        for i in range(1, n):
            LtoR[i] = max(LtoR[i - 1], height[i - 1])
            RtoL[n - 1 - i] = max(RtoL[n - i], height[n - i])

        # * Compute the amount of water that exists at each index
        for i in range(n):
            water += max(0, min(LtoR[i], RtoL[i]) - height[i])

        return water


sol: Solution = Solution()
print(sol.trap([2, 1, 3, 0, 1, 2, 3]))  # * 7
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # * 6
print(sol.trap([4, 2, 0, 3, 2, 5]))  # * 9
print(sol.trap([5, 0, 5]))  # * 5
print(sol.trap([0, 0, 0]))  # * 0

# * Time: O(n) - The time taken scales with the size of the input

# * Space: O(n) - We create two arrays (LtoR and RtoL), both of which scale with the input size (`n`)
