# 134. Gas Station

# * In a brute force manner, we can try starting from each of the indices
# * If (currGas + gas[i] - cost[i]) < 0, then we can't make the trip to the next station
# * Naturally, we need to track the number of stations we've visited so we know when we've looped
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # * We start at the finishing point
        if len(gas) == 1:
            return 0

        n: int = len(gas)

        # * Try every starting point
        for i in range(n):
            curr_gas: int = 0
            steps: int = 0

            # * From "i", loop back around to i
            for j in range(i, i + n):
                curr_gas += gas[j % n] - cost[j % n]

                # * You don't have the gas to make the trip
                if curr_gas < 0:
                    break

                steps += 1
                if steps == n:
                    return i

        return -1


sol: Solution = Solution()
print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # * 3
print(sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))  # * -1
print(sol.canCompleteCircuit([1, 1], [1, 1]))  # * 0

# * Time: O(n^2) - For each `i`, we perform an O(n) loop, which holds a nested O(n) loop

# * Space: O(1) - The memory usage remains constant regardless of input size
