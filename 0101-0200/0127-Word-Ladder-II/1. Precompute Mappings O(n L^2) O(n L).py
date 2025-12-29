# 127. Word Ladder

# * Instead of iterating over wordlist for each word and checking the hamming distance
# * We can precompute the patterns that each word will produce
# * For example, "hit" will produce:
# *     - "*ot", "h*t", and "ho*"
# * For each word, we essentially create an adjacency list of patterns -> word (neighbors)
# * Each word has the same length (L)
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # * Base Case - There is no possible path
        if endWord not in wordList:
            return 0

        # * pattern -> list of words it links to
        graph: dict[str, list[str]] = defaultdict(list)
        deq = deque([beginWord])
        L: int = len(beginWord)
        visited: set[str] = set([beginWord])
        transformations: int = 1

        wordList.append(beginWord)

        # * Build the L-length patterns for each word
        for word in wordList:
            for i in range(L):
                pattern: str = word[:i] + "*" + word[i + 1 :]
                graph[pattern].append(word)

        while deq:
            for _ in range(len(deq)):
                word: str = deq.popleft()

                # * Check for finished transformation
                if word == endWord:
                    return transformations

                # * Explore the neighbors (using patterns created from word)
                for i in range(L):
                    pattern: str = word[:i] + "*" + word[i + 1 :]

                    for neighbor in graph[pattern]:
                        if neighbor not in visited:
                            deq.append(neighbor)
                            visited.add(neighbor)

                    graph[pattern] = []

            transformations += 1

        return 0


# * Time: O(n * L^2) - The preprocessing step takes O(n * L^2), but the BFS itself is O(n * L)

# * Space: O(n * L) - The adjacency list's size scales with the number of words and the length of each word
