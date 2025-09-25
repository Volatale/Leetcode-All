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

        # * Try different offsets
        for i in range(word_len):
            left: int = i  # * Tracks the left of the window
            curr_count: Counter[str] = Counter()  # * No. of each word in window

            for right in range(i, n, word_len):
                word: str = s[right : right + word_len]

                if word in word_count:
                    curr_count[word] += 1

                    # * Validate the window (ensure we don't have too many of any words)
                    while curr_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]  # * Remove from window
                        curr_count[left_word] -= 1
                        left += word_len

                    # * If we have a valid window
                    if right - left + word_len == total_len:
                        indices.append(left)
                else:
                    curr_count.clear()  # ! Reset the window (word doesn't exist in `s`)
                    left = right + word_len  # * "right" failed, so move to next word

        return indices


sol: Solution = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))

# * Time: O(n * m) - Where `n` is the length of words[0] and `m` is the number of words

# * Space: O(m) - Where `m` is the number of words
