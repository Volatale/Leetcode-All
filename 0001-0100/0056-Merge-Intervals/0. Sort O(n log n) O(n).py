# 56. Merge Intervals

# * We are given an array of intervals where interval[i] = [start_i, end_i]
# * Our goal is to merge all of the overlapping intervals and return an array of the non-overlapping intervals
# ! Mathematically, an interval is overlapping if
# *     a.start <= b.end AND
# *     b.start <= a.end
# * Therefore the following intervals are considered overlapping:
# *     [1, 4], [4, 7]
# *     [1, 1], [1, 1]
# * Thus, intervals that end and start at the same point overlap (so we use <= and >=)
# ! To merge intervals, we take the minimum of the starts, and the maximum of the ends
# *     - Thus, a merger of [1, 7] and [0, 5] would result in [0, 7]
# ! In order to ensure monotonicity and ease of computation, we can sort the intervals based on their start times
# * Since the start times are monotonically non-decreasing, we don't have to compare the current interval with all of the rest
# * If we have [1, 5] and [6, 8] but we passed [0, 0], then because [6, 8] is AFTER [1, 5], we know that there cannot be an overlap here
# * So we want to keep the intervals sorted to avoid redundant checks
# *     - The alternative is checking the current interval against all of the other intervals in the results
# *     - And even then the merger of one interval can lazily result in subsequent mergers down the line
# *       It is also possible that some mergers are missed as a result (unless we forcefully merge the remaining ones)
# * Due to the fact that the input is sorted, we only have to compare against the most recent
# *     - if a[0] <= b[0] and b[0] <= c[0], then we can also say that a[0] < c[0], or, conversely, c[0] > a[0]

from functools import cmp_to_key


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) <= 1:
            return intervals

        # * Sort the intervals into ascending order by start time
        intervals.sort(
            key=cmp_to_key(
                lambda a, b: -1 if a[0] - b[0] < 0 else 1 if a[0] - b[0] > 0 else 0
            )
        )

        results: list[list[int]] = [intervals[0]]

        for i in range(1, len(intervals)):
            # * Get the most recent interval (since that's the one we need to merge with)
            prev: list[int] = results[-1]

            # * Check if there is an overlap; if there is, merge the most recent interval and the current
            if self.is_overlap(prev, intervals[i]):
                results[-1] = self._merge_intervals(prev, intervals[i])
            else:
                # * In the case of no overlap, we can simply push the interval to the top
                results.append(intervals[i])

        return results

    def is_overlap(self, a: list[int], b: list[int]) -> bool:
        return a[0] <= b[1] and b[0] <= a[1]

    def _merge_intervals(self, a: list[int], b: list[int]) -> list[int]:
        return [min(a[0], b[0]), max(a[1], b[1])]


sol: Solution = Solution()
print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(sol.merge([[1, 4], [4, 5]]))
print(sol.merge([[4, 7], [1, 4]]))
print(sol.merge([[1, 1], [1, 1]]))
print(sol.merge([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(sol.merge([[1, 4], [1, 2]]))
print(sol.merge([[1, 4], [1, 2], [2, 5]]))

# * Time: O(n log n) - The time taken to merge is likely O(n log n)
# * Additionally, we iterate over the entire array, which takes O(n)

# * Space: O(n) - In the worst case, the results array's size scales with the input size
# * It is possible that we return every interval if none overlap at all
