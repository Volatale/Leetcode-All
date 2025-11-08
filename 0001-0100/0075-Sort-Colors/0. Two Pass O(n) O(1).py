# 75. Sort Colors


# * We can use the dutch national flag algorthm here
# * The goal is to partition three distinct things by some criteria
# * Anything to the left of red is red
# * Anything to the right of blue is blue
# * So we need two pointers (red and blue) that act as boundaries
# * If white encounters a blue, we swap white and blue
# *     - Then blue decrements
# ! White is not immediately incremented because we don't know what blue pointed to
# *     - If blue pointed to a 1, then incrementing white here could lead to an invalid array
# * If white encounters a white, then we can simply increment white since no swap needs to happen yet
# * If white encounters a red, then white and red swap
# *     - Here, both red and white increment since we know for sure that there can't be a blue in this position
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n: int = len(nums)

        # * Used to count the no. of each color found
        red: int = 0
        white: int = 0
        blue: int = 0

        # * Count how many of each color we have
        for color in nums:
            if color == 0:
                red += 1
            elif color == 1:
                white += 1
            else:
                blue += 1

        # * Distribute the colors in order of priority (red, white, blue)
        for i in range(n):
            if red > 0:
                nums[i] = 0
                red -= 1
            elif white > 0:
                nums[i] = 1
                white -= 1
            elif blue > 0:
                nums[i] = 2
                blue -= 1


sol: Solution = Solution()
print(sol.sortColors([2, 0, 1]))
print(sol.sortColors([2, 0, 2, 1, 1, 0]))
print(sol.sortColors([2, 2, 2, 1, 1, 0, 0]))
print(sol.sortColors([1, 1, 2, 0]))
print(sol.sortColors([1, 1, 1]))
print(sol.sortColors([2, 1, 2, 1, 2, 1, 0, 1, 2]))

# * Time: O(n) - The time taken scales with the input size

# * Space: O(1) - The memory usage remains constant regardless of input size
