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

        # * Three pointers that each act as a boundary and swap index
        red: int = 0
        white: int = 0
        blue: int = n - 1

        while white <= blue:
            if nums[white] == 0:
                # * We can safely increment both because we know it can't be blue
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                # * Don't increment white, we don't know what blue pointed to yet
                nums[blue], nums[white] = nums[white], nums[blue]
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
