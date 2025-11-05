# 72. Edit Distance

# * There are a few different cases to consider
# * If word1[i] == word2[j], then no operation is needed
# *     - solve(i + 1, j + 1)
# * Otherwise, we need to try all three of the operations
# *     Insert = solve(i, j + 1) + 1 (insert word2[j] into word1)
# *     Delete = solve(i + 1, j) + 1 (remove word1[i])
# *     Replace = solve(i + 1, j + 1) + 1 (replace word1[i] with word2[j])
# ! If one of the strings has all of its characters expended, then we have to consider the remaining characters
# *     if i == n, then return (m - j)
# *         - We need to insert the remaining characters of word2 into word1
# *     if j == m, then return (n - i)
# *          - We need to delete the remaining characters of word1
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(i: int, j: int) -> int:
            # * Check for memoized subproblem
            if (i, j) in memo:
                return memo[(i, j)]

            # * Base Case: one string is fully traversed
            if i == n:
                return m - j  # * Inserting remaining chars of word2
            if j == m:
                return n - i  # * Delete remaining chars of word1

            # * We want the MINIMUM no. of operations
            operations: int = (1 << 31) - 1

            # * Case 1: Characters match (no operation needed)
            if word1[i] == word2[j]:
                operations = solve(i + 1, j + 1)
            else:
                # * Try all three operations
                insert_op = solve(i, j + 1) + 1  # * insert word2[j] into word1
                delete_op = solve(i + 1, j) + 1  # * remove word1[i]
                replace_op = solve(i + 1, j + 1) + 1  # * replace word1[i] with word2[j]
                operations = min(insert_op, delete_op, replace_op)

            memo[(i, j)] = operations
            return operations

        n, m = len(word1), len(word2)
        memo: dict[tuple[int, int], int] = {}
        return solve(0, 0)


sol: Solution = Solution()
print(sol.minDistance("horse", "ros"))  # * 3
print(sol.minDistance("ros", "horse"))  # * 3
print(sol.minDistance("intention", "execution"))  # * 5
print(sol.minDistance("son", "sonic"))  # * 2
print(sol.minDistance("sonic", "son"))  # * 2
print(sol.minDistance("sonic", "sonic"))  # * 0
print(sol.minDistance("son", "son"))  # * 0 (already equal)
print(sol.minDistance("", ""))  # * 0 (already equal)
print(sol.minDistance("mario", ""))  # * 5 removals
print(sol.minDistance("", "mario"))  # * 5 additions
print(sol.minDistance("sonic", "mario"))  # * 4 replacements
print(sol.minDistance("sonic", "mari"))  # * 1 deletion 3 replacements
print(sol.minDistance("peach", "peaci"))  # * 1 replacement

# * Time: O(n * m) - There are `n` possible values for `i` and `m` possible values for `j`
# * We are memoizing the result of each subproblem, so there are only (n * m) unique subproblems to solve

# * Space: O(n * m) - Since there are (n * m) unique subproblems, all of their results must be cached
