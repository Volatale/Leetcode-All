# 42. Trapping Rain Water

# * The biggest observation we need to make is that the water trappable at `i` depends on the left and right walls
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

# * We can use a two pointers approach nstead of computing the prefix and postfix arrays from left to right and right to left (of height)
# * Why does this work?
# * For the LtoR array, the values are always monotonically non-decreasing
# *     - That is, LtoR[i] <= LtoR[i + 1] for all i in LtoR
# * For the RtoL array, the values are always monotonically non-increasing
# *     - That is, RtoL[i] >= RtoL[i + 1] for all i in RtoL
# * Imagine we have [1, 2, 4, 2, 1]:
# *     - Once we hit index 1, we have a maximum left bar of height 1
# *     - Then, at index 2, we have a maximum left bar of height 2
# *         - Note that the bars in the indices [0..i - 1] are now useless
# *         - Thus, we ONLY care about the maximum we find in that direction
# ! The above observation is why two pointers works
# *     - Once we find a new maximum going in a specific direction, the previous bars become useless
# ! Remember that the reason the prefix postfix version works is that we know there is a FUTURE bar of a certain width
# *     - Hence we precompute in both directions (so we know the height of the largest bars to the left and right of each `i`)
# * Within each index, we want to improve the bottleneck (ala "Container with Most Water")
# *     - If left_max <= right_max, then we improve left_max
# *     - Otherwise, we improve right_max
# *     - If both are equal, then it doesn't matter which we improve because they can BOTH be considered the bottleneck


class Solution:
    def trap(self, height: list[int]) -> int:
        n: int = len(height)

        if n == 0:
            return 0

        # * Two pointers
        left: int = 0
        right: int = n - 1

        left_max: int = 0  # * Max height bar found going left to right
        right_max: int = 0  # * Ma height bar found going right to left

        water: int = 0

        while left <= right:
            if left_max <= right_max:
                # * There can't be any water here
                # * Right side is taller, so water at `left` depends on `left_max`
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1
            else:
                # * Left side is taller, so water at `right` depends on `right_max`
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1
        return water


sol: Solution = Solution()
print(sol.trap([2, 1, 3, 0, 1, 2, 3]))  # * 7
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # * 6
print(sol.trap([4, 2, 0, 3, 2, 5]))  # * 9
print(sol.trap([5, 0, 5]))  # * 5
print(sol.trap([0, 0, 0]))  # * 0

# * Time: O(n) - We perform one pass through the input and process every element once each

# * Space: O(1) - The memory usage remains constant regardless of the input size
