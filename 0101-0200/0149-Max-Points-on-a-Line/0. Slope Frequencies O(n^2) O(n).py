# 149. Max Points on a Line

# * Originally, for each point, we can think of checking 45 degree angles
# * However, for this problem we need to consider EVERY possible slope for every point
# * In other words, we need to check the collinearity of every node
# * The easiest way to do this is to use one of the following:
# *     - (Rise / Run) = (Change in Y) / (Change in X) = (y2 - y1) / (x2 - x1)
# * Naturally, this could result in a division by 0
# *     - To handle this case, we take the result of infinity (because otherwise we get an error)
# * We basically want to "tally up" the frequency of points that share the same slope
# * Then, we take the maximum of all of those frequencies
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        # * There is only 1 point
        if len(points) == 1:
            return 1

        n: int = len(points)
        longest: int = 1  # * We are guaranteed at least one point

        for i in range(len(points)):
            x1, y1 = points[i]
            freq: dict[float, int] = {}  # * Slope -> Frequency

            # * Get the slope between every other point
            for j in range(i + 1, n):
                x2, y2 = points[j]

                # * If x1 == x2, they form a vertical line (0 slope)
                slope: float = (1 << 31) - 1 if x1 == x2 else (y2 - y1) / (x2 - x1)

                freq[slope] = (freq.get(slope) or 0) + 1
                longest = max(longest, freq[slope] + 1)

        return longest


# * Time: O(n^2) - For each point, we need to consider every other point

# * Space: O(n) - For each outer iteration, there are essentially `n` unique keys in the worst case
