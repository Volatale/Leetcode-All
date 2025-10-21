# 57. Insert Intervals

# * The intervals can be categorized as such:
# *     - Intervals that END before the new interval STARTS
# *     - Intervals that overlap with the new interval
# *     - Intervals th at START after the new interval ENDS
# * Based on this logic, we can simply push all of the non-overlapping intervals to the results array
# * Then, we know there will be some intervals that overlap since they weren't pushed
# *     - These intervals must be merged as we come to them
# * Then, we can push all of the intervals that start after the new interval ends
class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        # * If the array is empty there are no conflicts
        if len(intervals) == 0:
            return [newInterval]

        # * Start with an array of the first interval in the list
        results: list[list[int]] = []
        i: int = 0
        n: int = len(intervals)

        # * Add intervals that END before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            results.append(intervals[i])
            i += 1

        # * Merge intervals that overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        results.append(newInterval)

        # * Add intervals that START after newInterval ends
        while i < n:
            results.append(intervals[i])
            i += 1

        return results


sol: Solution = Solution()
print(sol.insert([[1, 3], [6, 9]], [2, 5]))
print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(sol.insert([[1, 2], [3, 4], [5, 6], [7, 8]], [9, 10]))
print(sol.insert([[1, 1], [1, 1], [1, 1]], [1, 1]))
print(sol.insert([[1, 2], [2, 3]], [3, 4]))
print(sol.insert([], [1, 10]))
print(sol.insert([[1, 10]], [0, 11]))

# * Time: O(n) - The time taken scales with the input size, we process each interval once at most

# * Space: O(n) - In the worst case, there are no overlaps and thus we return an array of size n
