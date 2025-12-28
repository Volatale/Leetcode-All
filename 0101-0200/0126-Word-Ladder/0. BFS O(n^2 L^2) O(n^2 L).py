# 126. Word Ladder II

# ! THIS WON'T PASS ON LEETCODE

# * We want ALL of the shortest transformation paths from `beginWord` to `endWord`
# * It is still possible to use BFS here (and we should)
# *     - However, we need to make some modifications...
# * We can no longer solely rely on a global `visited` set
# *     - Why? Because the same node could exist in multiple shortest paths
# *     - So we can't simply mark a node as visited after visiting it
# ! Instead, we can utilize an extra visited set, that tracks the visitedness ONLY for the CURRENT layer
# *     - Then, once we have explored the current frontier, we can add this frontier's visited nodes to the global visited set
from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:
        # * Base Case -> There is no possible path
        if endWord not in wordList:
            return []

        L: int = len(beginWord)
        wordList.append(beginWord)

        results: list[list[str]] = []
        graph: dict[str, list[str]] = defaultdict(list)
        deq = deque([(beginWord, [beginWord])])  # * word, path
        visited: set[str] = set([beginWord])
        found_shortest: bool = False

        # * Build the L-length patterns for each word
        for word in wordList:
            for i in range(L):
                pattern: str = word[:i] + "*" + word[i + 1 :]
                graph[pattern].append(word)

        while deq and not found_shortest:
            # * A frontier-level visited set
            next_level_visited: set[str] = set()

            for _ in range(len(deq)):
                word, path = deq.popleft()

                # * Check for finished transformation
                if word == endWord:
                    results.append(path)
                    found_shortest = True  # * A shortest path exists
                    continue

                for i in range(L):
                    pattern: str = word[:i] + "*" + word[i + 1 :]

                    for neighbor in graph[pattern]:
                        if neighbor not in visited:
                            next_level_visited.add(neighbor)  # * Visited in THIS layer
                            deq.append((neighbor, path + [neighbor]))

            # * Add the nodes visited in this layer to the global visited
            visited |= next_level_visited

        return results


sol: Solution = Solution()
print(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(sol.findLadders("sonic", "sonia", ["sonia"]))

# * Time: O(n^2 * L^2) - It takes O(n * L^2) to generate all of the wildcard patterns
# * Within the BFS itself, in the worst case, we have to create a new path array that can be of length `n`

# * Space: O(n^2 * L) - For each key, we potentially have to store both a string AND a path of length `n`
