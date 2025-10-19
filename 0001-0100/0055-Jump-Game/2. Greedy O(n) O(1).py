# * 55. Jump Game

# * Our goal is to reach the last index (n - 1) one way or another
# * From each index, we can jump between [1, nums[i]] times
# * Thus, we have a set of indices we can reach from some index `i`
# * For example, if we have [2, 3, 4]
# *     - From index 0, we can reach {1, 2}
# *     - From index 1 we can reach {2}
# * This behaviour is reminiscent of how a graph network works with BFS
# * At each index, we have a set of indices (nodes/vertices) we can reach
# * We don't necessarily want the shortest path, but a BFS approach would lead to that anyway
# * In a greedy manner, we can simply track the furthest index reachable
# * And if that index >= n - 1, then we know we can reach the last index
# *     - If we were 2 away from n - 1, and we made a jump of 3
# *       We'd overshoot, but we can easily just jump one less and make it to n - 1
# * We can track the furthest reachable index because we know there's a path there "somehow"
# *     - The exact path we need to take is irrelevant
# *     - All we care about is whether the index is reachable or not
# * If i > furthest, then we know n - 1 is not reachable
# * For example, if we have [2, 0, 0, 1]
# *     - i = 0, we can reach index 2 at most
# *         - So furthest = 2
# *     - Now i = 1, and furthest is still 2
# *     - Now i = 2, and furthest is STILL 2
# * If we had [2, 0, 1, 1]:
# *     - At i = 0, we can reach 2 at most
# *         - furthest = 2
# *     - At i = 1, we can reach 2 at most
# *     - At i = 2, we can reach 3 at most
# *         - furthest = 3 (which means we can return true)
# ! Notice how the path itself was irrelevant
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n: int = len(nums)
        furthest: int = 0  # * The furthest index we can travel to

        for i in range(0, n):
            # * We are stuck and thus cannot reach n - 1
            if i > furthest:
                return False

            # * Check if we have a new best
            furthest = max(furthest, i + nums[i])

            # * Successfully reached index n - 1
            if furthest >= n - 1:
                return True

        # * We failed to reach index n - 1
        return False


sol: Solution = Solution()
print(sol.canJump([1, 1, 1]))
print(sol.canJump([2, 3, 1, 1, 4]))  # * True
print(sol.canJump([3, 2, 1, 0, 4]))  # * False
print(sol.canJump([3, 1, 0, 0, 1, 0, 0]))  # * False
print(sol.canJump([1, 0, 0, 2]))  # * False
print(sol.canJump([4, 0, 0, 0, 0]))  # * True
print(sol.canJump([2, 3, 1, 10, 0, 0, 0, 4]))  # * True

# * Time: O(n) - We iterate over the entire array and process each element once

# * Space: O(1) - The memory usage remains constant regardless of input size
