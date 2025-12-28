# 126. Word Ladder II


# * We want ALL of the shortest transformation paths from `beginWord` to `endWord`
# * It is still possible to use BFS here (and we should)
# *     - However, we need to make some modifications...
# * We can no longer solely rely on a global `visited` set
# *     - Why? Because the same node could exist in multiple shortest paths
# *     - So we can't simply mark a node as visited after visiting it
# ! Instead, we can utilize an extra visited set, that tracks the visitedness ONLY for the CURRENT layer
# *     - Then, once we have explored the current frontier, we can add this frontier's visited nodes to the global visited set
# ! The biggest change is that we need to use BFS to form a shortest path DAG
# * Using that shortest path DAG, we can then use backtracking/DFS to enumerate every path
# *     - Since we'd be starting at `endWord`, we simply reverse the paths as we find them
from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:
        # * Base Case -> There is no possible path
        if endWord not in wordList:
            return []

        L: int = len(beginWord)

        # * Precompute pattern -> words list
        graph: defaultdict[str, list[str]] = defaultdict(list)
        # * Used to reverse engineer the path at the very end
        parents: defaultdict[str, list[str]] = defaultdict(list)
        results: list[list[str]] = []
        visited: set[str] = set([beginWord])
        deq = deque([beginWord])
        found_end: bool = False

        for word in wordList + [beginWord]:
            for i in range(L):
                pattern: str = word[:i] + "*" + word[i + 1 :]
                graph[pattern].append(word)

        # * BFS to build the adjacency list (DAG) ONLY containing shortest paths
        while deq and not found_end:
            # * A visited set that is only relative to the current frontier
            next_level: set[str] = set()

            for _ in range(len(deq)):
                word: str = deq.popleft()

                for i in range(L):
                    pattern: str = word[:i] + "*" + word[i + 1 :]

                    for neighbor in graph[pattern]:
                        if neighbor not in visited:
                            # * Found a shortest path
                            if neighbor == endWord:
                                found_end = True

                            if neighbor not in next_level:
                                next_level.add(neighbor)  # * Visited in THIS layer
                                deq.append(neighbor)
                            parents[neighbor].append(word)
            # * Add the visited nodes from this frontier to the global visited nodes
            visited |= next_level

        # * No path exists
        if not found_end:
            return []

        # * Backtrack all paths from endWord -> beginWord
        path: list[str] = [endWord]

        def dfs(word: str):
            # * Base Case
            if word == beginWord:
                results.append(path[::-1])
                return

            for p in parents[word]:
                path.append(p)  # * Choose candidate
                dfs(p)  # * Explore path
                path.pop()  # * Unchoose candidate

        dfs(endWord)
        return results


sol: Solution = Solution()
print(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(sol.findLadders("sonic", "sonia", ["sonia"]))

# * Time: O(n^2 * L + k * N)

# * Space: O(n^2 * L)
