# * 30. Substring with Concatenation of All Words

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # * Handles the empty `s` or empty `words` array
        if not s or not words:
            return []

        word_len: int = len(words[0])
        total_len: int = word_len * len(words)
        word_count: Counter[str] = Counter(words)  # * The max no. of each word
        n: int = len(s)
        indices: list[int] = []

        for i in range(n - total_len + 1):
            substring = s[i : i + total_len]

            # * Split the current substring up into word_len chunks
            chunks = [
                substring[j : j + word_len] for j in range(0, total_len, word_len)
            ]

            # * We found an exact match
            if Counter(chunks) == word_count:
                indices.append(i)

        return indices


sol: Solution = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))

# * Time: O(n * m * word_len) - Where `n` = len(s), `m` = len(words)

# * Space: O(m) - Where `m` is the number of words
