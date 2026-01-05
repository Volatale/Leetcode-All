# 135. Candy

# * It is important to note that the ratings are only relative to the adjacent neighbors
# ! Essentially, the ratings act as WEIGHTS, not necessarily a ratio
# * If we have [1, 3], that doesn't mean that ratings[1] gets 3x more candies than ratings[0]
# !     - In other words, the ratings are NOT multipliers
# * Each child is supposed to get 1 candy MINIMUM, thus we should start with len(ratings) candies
# * It is impossible to handle both directions at once, so we need to do multiple passes
# * The first pass is a forward pass that determines whether ratings[i] > ratings[i - 1]
# *     - If that is the case, then we know ratings[i] should get one more candy than ratings[i - 1]
# * The second pass is a backward pass that determines whether ratings[i] > ratings[i + 1]
# *     - Like in the forward pass, if ratings[i] > ratings[i + 1], then ratings[i] should get 1 more candy
# * We want to distribute the MINIMUM amount of candies possible
# * Therefore, relative to each child and their neighbors, they should get ONE more than the lower side
# *     - Unless of course, one more than the lower side is less than what they already have
# *     - Hence the use of max() in the second pass


class Solution:
    def candy(self, ratings: list[int]) -> int:
        n: int = len(ratings)
        candies: list[int] = [1] * n  # * Each child gets 1 candy minimum

        # * Handle the weights in the <-- direction
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # * Handle the weights in the ---> direction
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


sol: Solution = Solution()
print(sol.candy([1, 0, 2]))  # * 5
print(sol.candy([1, 2, 2]))  # * 4
print(sol.candy([1, 1, 1]))  # * 3
print(sol.candy([5]))  # * 1
print(sol.candy([0, 0]))  # * 2
print(sol.candy([1, 2, 3, 4, 5]))  # * 15
print(sol.candy([5, 4, 3, 2, 1]))  # * 15

# * Time: O(n) - We perform two passes over the entire input

# * Space: O(n) - The memory usage scales with the size of the input
