# 139. Word Break

# * We are just trying to reach index `n` by using words in `wordDict`
# * This can be optimized via Dynamic Programming due to the following reasons:
# *     - Subproblems are only dependent one way (dp[i] depends on dp[i + len(substring)])
# *     - We are trying to `optimize` our path such that we can complete it in general (not necessarily in the minimum steps)
# * Thus, we have Overlapping Subproblems and Optimal Substructure
# ! We iterate backwards because in the recursive version, we iterated bottom-up
# *     - Thus the subproblems must be computed in top-down order for the iterative version
class Trie:
    def __init__(self, words: list[str] = []):
        self.root = TrieNode()

        for word in words:
            self.insert(word)

    def insert(self, word: str):
        curr: TrieNode = self.root

        # * Create a new child node for non-existent characters
        for char in word:
            # if curr.children.get(char) is None:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr: TrieNode = self.root

        for char in word:
            # * The word does not exist in the Trie
            if char not in curr.children:
                return False

            curr = curr.children[char]

        return curr.is_end_of_word


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n: int = len(s)
        trie: Trie = Trie(wordDict)

        # * dp[i] = Whether `j` exists such that s[i:j+1] in dict, and dp[j + 1] == True
        dp: list[bool] = [False] * (n + 1)
        dp[n] = True  # * It is always possible to create an empty string

        # * Keep extending from `i` to create substrings
        for i in range(n - 1, -1, -1):
            curr: TrieNode = trie.root

            for j in range(i, n):
                # * The prefix s[i:j+1] isn't present in wordDict
                if s[j] not in curr.children:
                    break

                curr = curr.children[s[j]]

                if curr.is_end_of_word and dp[j + 1]:
                    dp[i] = True
                    break

        return dp[0]


sol: Solution = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))  # * True
print(sol.wordBreak("sonic", ["s", "o", "n", "i", "c"]))  # * True
print(sol.wordBreak("shadow", ["shadow"]))  # * True
print(sol.wordBreak("a", ["b"]))  # * False
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # * False

# * Time: O(n^2) - Initializing the Trie takes O(n * L), where `L` is the length of the longest word in `wordDict`
# * Then, we have two nested for loops, both of which scale with `n`
# * The main benefit of the Trie is that prefix lookups can be handled in O(1)

# * Space: O(n * L) - In the worst case, every word in `wordDict` is the same length
# * So if there are 5 words, each of length 4, there are (5 * 4) TrieNodes
