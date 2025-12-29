# 127. Word Ladder

# * The goal is to find the shortest path to transform `beginWord` into `endWord`
# * Naturally, this is a good usecase for breadth-first search
# * We can use the hamming distance algorithm to determine which words differ by a single character for each word
# * Instead of using tuples of (word, transformations), we can instead use a level-order traversal approach
# * Every level, we increment "transformations" by one
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        def hamming_distance(curr: str, word: str) -> bool:
            diffs: int = 0  # * The no. of chars that are different

            for i in range(len(word)):
                if word[i] != curr[i]:
                    diffs += 1

            # * The distance must be exactly equal to 1
            return diffs == 1

        # * Base Case - Both are immediately equal
        if beginWord == endWord:
            return 0

        # * Base Case - There is no path to the final word
        if endWord not in wordList:
            return 0

        deq = deque([beginWord])
        transformations: int = 0
        visited: set[str] = set()

        while deq:
            size: int = len(deq)

            # * Level-order Traversal
            for _ in range(size):
                curr = deq.popleft()

                # * Check for finished transformation
                if curr == endWord:
                    return transformations + 1

                # * Find potential children
                for word in wordList:
                    if word not in visited and hamming_distance(curr, word):
                        deq.append(word)
                        visited.add(word)  # * Stops deq from containing duplicates

            transformations += 1

        return 0


# * Time: O(n^2 * L) - For each popped word, we linearly scan every word in `wordList` and check hamming distance
# * That's O(N * L) per node; in the worst case, BFS explores most of the list, which gives us O(n^2 * L)

# * Space: O(n) - In the worst case, the number of words in the deque and the size of the visited set are equal to wordlist
