# 137. Single Number II

# * In a situation where each element appears TWICE except for one, we could use XOR
# *     - Why? Because we only need two states for each bit position
# *     - So XOR-ing the entire array means we'll eventually be left with the single-occurrence element
# * Since each element only appears twice, for each bit position (0-31):
# * If the unique number has a 1 in this position, the total count of 1s in that position across the whole array is (2k + 1)
# * If the unique number has a 0 in this position, the total count of 1s in that position across the whole array is 2k
# * This logic can be extended for elements that appear THREE times, it simply becomes:
# *     - 1 in ith position -> 3k + 1 (1s)
# *     - 0 in ith position -> 3k (1s)
# * We can't simply take the prefix XOR of the entire array using a single variable since we need THREE possible states
# * And since we need THREE states, that is essentially the same as a modulo 3 (0 -> 1 -> 2 -> 0)
# ! Thus, we can just add an extra variable to track the extra state
# *     - `ones` is used to track the bits in each position that has only occurred ONCE
# *     - `twos` is used to track the bits in each position that has occurred TWICE
# * Based on this logic, for each bit position `i`, ones[i] != twos[i]
# *     - If this logic were NOT upheld, then you'd be saying that the ith bit has been found once AND twice
# *       which doesn't make sense given that we want "modulo 3" behavior
# * Thus, we need to & by the negation of the opposite state
# *     ((0 ^ 4) & ~ones) means "toggle the necessary bits, but keep only the bits that AREN'T set in twos"
# *     ((0 ^ 4) & ~twos) means the same as the above, but flipped
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones: int = 0  # * Holds all bits whose count mod 3 is currently 1
        twos: int = 0  # * Holds all bits wose count mod 3 is currently 2

        # * XOR toggles, but & by the negation ensures ones[i] != twos[i] (breaks mod logic)
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones

        return ones


# * Time: O(n) - We perform a single pass through the entire input

# * Space: O(1) - The memory usage remains constant reardless of input size
