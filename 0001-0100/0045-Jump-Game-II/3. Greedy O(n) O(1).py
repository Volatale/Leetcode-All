# 45. Jump Game II

# * Fundamentally, this is a shortest path problem
# * The goal is to use the minimum amount of jumps necessary to reach index n - 1
# * Shortest paths problems are usually solved using BFS
# ! However, a regular BFS implementation with a queue will still end up being O(n^2)
# *     - Why? Because we still have to compute every possible jump
# *     - Which means iterating between 1..nums[i] times from each node
# * Instead, we can use the same style of approach, but use the indices to represent nodes
# * Lets say we have [2, 3, 1, 0, 1]
# *     - From index 0, we can reach indices in the range [1, 2]
# *     - Therefore, the first "frontier" (layer) spans (0 + 2) indices (or nodes)
# ! The FURTHEST we can reach from index 0 is index 2, so we keep track of this
# *     - This index is essentially the index wherein the frontier ends
# *     - That is, any greater index is part of a different frontier
# * When we reach the index that marks the end of our frontier, we are forced to make a jump
# *     - Thus, when i == end, jumps += 1, and end = farthest
# *     - Remember that farthest is the END of the current frontier
# *         - So by setting end = farthest, we know exactly when the next frontier will end
class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps: int = 0
        end: int = 0  # * Marks the end of the current frontier
        farthest: int = 0

        for i in range(len(nums) - 1):
            # * The furthest index we can currently get to
            farthest = max(farthest, i + nums[i])

            # * If i == end we have finished the current frontier
            if i == end:
                jumps += 1  # * We only jump when absolutely necessary
                end = farthest  # * We now have a new frontier end

        # * The min. no of jumps necessary to get to index n - 1
        return jumps


sol: Solution = Solution()
print(sol.jump([2, 3, 1, 1, 4]))  # * 2
print(sol.jump([1, 1, 1]))  # * 2
print(sol.jump([4]))  # * 0
print(sol.jump([1, 2, 1, 2, 1, 2]))  # * 3
print(sol.jump([2, 3, 0, 1, 2]))  # * 2
print(sol.jump([2, 3, 1, 0, 1, 3]))  # * 2

# * Time; O(n) - The time taken scales with the length of the input
# * We process each element once each (minus the last)

# * Space: O(1) - The memory usage remains constant regardless of input size
