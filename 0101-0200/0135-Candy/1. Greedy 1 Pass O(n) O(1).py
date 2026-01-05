# 135. Candy

# * We required two passes in the candy array version
# * Why? Because you can't possible know both:
# *     - The left-neighbor requirements
# *     - AND the right-neighbor requirements at the same time
# * Thus, we needed to perform two passes over the array
# * The array-less version replaces per-child candy storage with run lengths
# *     - These are directional, but self-contained
# * We need to track the length of both the increasing AND the decreasing runs
# * Additionally, we need to track the height of the highest peak so far
# * Why? Because in a situation like [1, 2, 3, 2, 1, 0]
# *     - The increasing sequence is [1, 2, 3]
# *     - The decreasing sequence is [3, 2, 1, 0]
# !     - The 3 is counted twice
# * That means we get (1 + 2 + 3) candies for the increasing run
# * And (1 + 2 + 3 + 4) candies for the decreasing run, but there's a problem
# * Since the length of the decreasing run is 4, that is a LOWER value than what the heighest peak actually is (3)
# * So it is an incorrect decision to add an extra candy to index 5, so we instead add it to the peak
# *     - This is handled via (if down >= peak -> total += 1)
# ! The increasing sequence is like (1 + 2 + 3 + ... + k)
# ! And the decreasing sequence is the same... but with one caveat
# *     - We iterate forward, so the decreasing sequence is essentially supposed to be calculated in reverse
# * Regardless, if you mentally swap the decreasing sequence (1, 2, 3) instead of (3, 2, 1) then it still works out
# *     - Either way, the correct number of candies are distributed
# * You know the increasing sequence the moment you FIND it
# * You know the decreasing sequence the moment it ENDS
# * All contributions are handled immediately

# ! Simply put, candy assignment is the sum of the sizes of all "stairs"
# * For increasing runs:
# *     - Ratings = [1, 2, 3, 4]
# *     - Candies = [1, 2, 3, 4] (sum = 10)
# * For decreasing runs:
# *     - Ratings = [4, 3, 2, 1]
# *     - Candies = [4, 3, 2, 1] (sum = 10)
# * For a peak:
# *     - Ratings = [1, 2, 3, 2, 1, 0]
# *     - Increasing run = (1, 2, 3), so length 3
# *     - Decreasing run = (2, 1, 0), so length 3 (an equal length run)
# * If a down-slope is as long as or is longer than the up-slope, we add one extra candy
# * Lets say you have [1, 2, 3, 4, 3, 2, 1, 0]
# *     - Increasing run = (1, 2, 3, 4)
# *     - Decreasing run = (4, 3, 2, 1)
# !     - That gives us (1 + 2 + 3 + 4) candies and (1 + 2 + 3 + 4) candies
# *     - So the peak amount (4) is added twice, thus meaning we don't technically have a peak
# *         - To fix this, we have to add one if the down-length run is >= peak
# * If you have ->   [1, 2, 3, 4, 3, 2, 1, 0]
# * The candies are: [1, 2, 3, 4, 3, 2, 1, 0], but each child need to get one candy MINIMUM, hence we add one
# *     - This gives us [1, 2, 3, 4, 3, 2, 1, 1]


class Solution:
    def candy(self, ratings: list[int]) -> int:
        total: int = 1
        increasing: int = 1  # * Length of current increasing run
        decreasing: int = 0  # * Length of current decreasing run
        peak: int = 1

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                increasing += 1  # * Sequence extends by 1 element
                peak = increasing  # * We have a new peak (so far)
                decreasing = 0  # * Reset the decreasing run
                total += increasing  # * Add the contribution for this run
            elif ratings[i] < ratings[i - 1]:
                decreasing += 1
                increasing = 1
                total += decreasing

                if decreasing >= peak:
                    total += 1  # * Add 1 to avoid counting the peak twice
            else:
                # * Equal on both sides, reset counts for the new mountain
                increasing = 1
                decreasing = 0
                peak = 1
                total += 1  # * This child gets the minimum possible (1)

        return total


sol: Solution = Solution()
print(sol.candy([1, 2, 3, 3, 3, 1]))  # * 10
print(sol.candy([1, 0, 2]))  # * 5
print(sol.candy([1, 2, 2]))  # * 4
print(sol.candy([1, 1, 1]))  # * 3
print(sol.candy([5]))  # * 1
print(sol.candy([0, 0]))  # * 2
print(sol.candy([1, 2, 3, 4, 5]))  # * 15
print(sol.candy([5, 4, 3, 2, 1]))  # * 15

# * Time: O(n) - We perform a single pass over the entire input, so the time taken scales linearly

# * Space: O(1) - The memory usage remains constant regardless of input size
