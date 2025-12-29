# 127. Word Ladder

# * Here, we use the precomputed pattern approach along with a bidirectional BFS
# * Regular BFS works because we want to get from A to B
# * But we could also get from B to A...
# * Based on this, why not search from both sides simultaneously and meet in the middle?
# ! Why can we use sets instead of queues (or deques)?
# *      Word ladder adjacency isn't graph-like in need of FIFO
# *      Neighbors come from wildcard expansion, not from dynamic branching order
# *      All neighbors of the frontier nodes form the next frontier regardless of order
# *      Thus, a deque adds no benefit
# * Bidirectional BFS works because the paths are reversible
# *      A path from A -> B is the same length as a path from B -> A
# *      So instead of searching the whole space outward from one side, you grow two trees that ideally meet in the middle
# *      This reduces the complexity from O(b^d) to O(b^(d/2)) + O(b^(d/2))
# * Adjacency is wildcard-based, not positional BFS-based
# *      There is no "branching structure" where order matters - all neighbors in the same level are equally likely to expand
# *      Since we expand entire frontiers at once (as a batch), a set is all you need:
# *         - No FIFO needed
# *         - No ordering needed
# *         - Just "who is in the current layer"
# *      Thus, a deque is unnecessary overhead
# * Sets naturally prevent duplicate frontier entries
# *      In a normal BFS, you prevent duplicate queue pushes by marking nodes as visited
# *      However, a set simplifies this for us...
# *         - A set automatically avoids duplicates
# *         - We merge neighbors into a set for the next layer, so repeats collapse automatically
# * Expanding the smaller frontier is the key to optimization
# *      At each step, we have `begin_set` and `end_set`
# *      If one side has far fewer words, expanding it will:
# *         - Explore fewer wildcard expansions
# *         - Touch fewer adjacency lists
# *         - Shrink the search dramatically
# *      And since the search meets in the middle, exploring the small side is always optimal
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # * Base Case: There is no possible path to endWord
        if endWord not in wordList:
            return 0

        L: int = len(beginWord)
        graph: defaultdict[str, list[str]] = defaultdict(list)
        begin_set: set[str] = set([beginWord])
        end_set: set[str] = set([endWord])
        visited: set[str] = {beginWord, endWord}
        transformations: int = 1

        # * Precompute the patterns and their mappings
        for word in wordList:
            for i in range(L):
                pattern: str = word[:i] + "*" + word[i + 1 :]
                graph[pattern].append(word)

        while begin_set and end_set:
            # * Always expand the smaller frontier
            if len(begin_set) < len(end_set):
                begin_set, end_set = end_set, begin_set

            next_level: set[str] = set()

            for word in begin_set:
                for i in range(L):
                    pattern: str = word[:i] + "*" + word[i + 1 :]

                    for neighbor in graph[pattern]:
                        # * Found the path to endWord
                        if neighbor == endWord:
                            return transformations + 1

                        if neighbor not in visited:
                            visited.add(neighbor)
                            next_level.add(neighbor)

            begin_set = next_level
            transformations += 1

        return 0


sol: Solution = Solution()
print(sol.ladderLength("hit", "got", ["hot", "got"]))
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

# * Time: O(N * L^2) - It takes O(n * L^2) to generate all of the wildcard patterns for each word in `wordList`

# * Space: O(N * L) - There are `N` words, each producing `L` patterns; in the worst case, each pattern is unique
# * Thus, there are N * L pattern keys, and each key can store all `N` words -> O(N * L)
# * Additionally, the visited sets and 2 frontiers use O(n) space
