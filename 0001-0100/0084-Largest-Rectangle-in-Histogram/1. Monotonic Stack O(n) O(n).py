# 84. Largest Rectangle in Histogram

# * If we have a series of ascending values like [1, 2, 3]
# * Then as we expand the range of elements, the product will either stay the same or increase
# ! The product will never DECREASE in this case
# * For example (height, width):
# *     (1 * 1) = 1 [1]
# *     (1 * 2) = 2 [1, 2]
# *     (1 * 3) = 3 [1, 2, 3]
# * So we want to keep expanding until we find an element < the most recent
# * Most recent means we should probably use a LIFO algorithm
# * And since we care about the values specifically, and we're popping with a condition based on that value
# ! Thereore, a monotonic stack is a useful data structure here
# * Additionally, we need to handle the following cases:
# *     Case 1: All elements are monotonically non-decreasing (so the inner while loop condition is never triggered)
# *     Case 2: At the end of the algorithm, there are still elements within the stack
# * We should force an activation of the condition in both of these cases
# * In the case of the first, we should also use a sentinel value like -1

# * How does the while loop work?
# * Keep iterating until we find an element < the most recent (stack[-1])
# *     In other words, we want to find the next smaller element
# * When we do, we know that index `i` is the index of the next smaller element
# * And the element on top of the stack is the previous greater element
# * Thus, height[stack[-1]] gives us the HEIGHT of the previous greater element
# *     Now we just need the width
# * We don't include the current element (bar) in the calculation (the current i), hence we need to subtract by 1
# * And we also want to exclude the elements before the previous greater element
# * So stack[-1] is the left of the range, and `i` is the right of the range (of [0, i])
# ! (right - 1) - (stack[-1] + 1) + 1
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area: int = 0
        stack: list[int] = [-1]  # * Monotonically non-decreasing stack
        heights.append(0)  # * Sentinel value to force inner while loop block

        for i in range(len(heights)):
            # * Process elements when we find an element < top of stack
            while stack and heights[i] < heights[stack[-1]]:
                height: int = heights[stack.pop()]

                # * index of NSE (i) bar -
                width: int = i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        heights.pop()  # * Remove sentinel
        return max_area


sol: Solution = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # * 10
print(sol.largestRectangleArea([1, 1, 1]))  # * 3
print(sol.largestRectangleArea([2, 4]))  # * 4
print(sol.largestRectangleArea([1]))  # * 1

# * Time: O(n) - Each element in the array is processed twice at most

# * Space: O(n) - In the worst case, the stack's size grows linearly with the input size
# * If we have [1, 2, 3], then there are no monotonically decreasing elements, thus the stack is [0, 1, 2]
