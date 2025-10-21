# 57. Insert Intervals


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        # * If the array is empty there are no conflicts
        if len(intervals) == 0:
            return [newInterval]

        # * Start with an array of the first interval in the list
        results: list[list[int]] = []

        for interval in intervals:
            # * Case 1: New interval starts after current interval ends (no overlap)
            if newInterval[0] > interval[1]:
                results.append(interval)
            elif newInterval[1] < interval[0]:
                # * Case 2: New interval ends after the current interval starts (no overlap)
                results.append(newInterval)
                newInterval = interval
            else:
                # * Merge intervals (we have an overlap)
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]

        results.append(newInterval)
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
