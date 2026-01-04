# 134. Gas Station

# * In a brute force manner, we can try starting from each of the indices
# * If (currGas + gas[i] - cost[i]) < 0, then we can't make the trip to the next station
# * Naturally, we need to track the number of stations we've visited so we know when we've looped
# ! However, fundamentally, we cannot make a circular trip from ANY index if sum(gas) < sum(cost)
# * Thus, with that understanding, we can actually apply a greedy approach
# * As we go, track the total gas and total cost overall
# *     - We can use this as a final check to check for the validity
# * If the accumulated (gas[i] - cost[i]) pairs is < 0
# *     - Then we cannot possibly have started where we did
# *     - Hence, we try starting at i + 1
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n: int = len(gas)

        start: int = 0  # * A possible starting point
        total_gas: int = 0
        total_cost: int = 0
        curr_gas: int = 0  # * Accumulated (gas[i] - cost[i]) pairs

        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]
            curr_gas += gas[i] - cost[i]

            # * Can't make the trip; move on and reset gas
            if curr_gas < 0:
                curr_gas = 0
                start = i + 1

        return start if total_gas >= total_cost else -1


sol: Solution = Solution()
print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # * 3
print(sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))  # * -1
print(sol.canCompleteCircuit([1, 1], [1, 1]))  # * 0

# * Time: O(n) - We perform `n` iterations overall, so the time taken scales with the input size

# * Space: O(1) - The memory usage remains constant regardless of input size
