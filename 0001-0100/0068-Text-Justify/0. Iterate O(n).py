# 68. Text Justification

# * For each line, greedily add as many words as possible
# * line_length gives us the total amount of characters among all words in the line
# ! We must add at least 1 space between each word in a line
# *     - The description says the words on each line must be left and right justified
# * Remember that if we simply push each word to an array and join it, we'll get: ["a", "b", "c"] -> "abc"
# *      - But there should be gaps between the words like in ("a b c") or something to that effect
# * For example, if we have [a, b, c] and the current word is d, maxWidth = 6
# *     - This is what we currently have at minimum: "a b c"
# *     - As you can see, line_length = 3, and len(line) = 3
# *         - line_length + len(word) + len(line) <= maxWidth?
# *         - 3 + 1 + 3 > 6, so we can't add the current word (d)
# *     - That would give us "a b c d" on one line. There are 4 words, so there are 4 - 1 spaces
# ! If the length of the line is 1, then there are two possibilities:
# *     - EIther this is the final line
# *     - We can't add anything else to this line (thus there is only 1 word)
# * We handle both of the above cases the same way
# *     - Add all of the space on the right (left justify the word)
# * Otherwise, we need to distribute the space
# ! The amount of spaces we need is given by (maxWidth - line_length)
# ! The amount of gaps we need is given by len(line) - 1
# *     - Imagine we have [a, b, c]. len(line) = 3, and there are two gaps
# *     - Or, if we have ["sonic", "the", "hedgehog", "is", "cool"], len(line) = 5, and there are 4 gaps (5 - 1)
# * We have to distribute the amount of spaces we have evenly among those gaps
# *     - spaces // gaps (we floor because we can't have a fraction of a gap)
# *     - The quotient here is the MINIMUM amount of space that gets applied to each gap (excluding the extras)
# * If we can't evenly divide the spaces among the gaps, we'll end up with some extras
# *     - spaces % gaps (this is the amount of extra space that wasn't evenly divided)
# ! If we have extra spaces left over, we need to distribute those evenly too
# *     - The extra space is frontloaded on a first-come-first-serve basis
# *     - So the total space distributed per gap is: (" " * even_space + (1 if j < gaps else 0))
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        i: int = 0
        result: list[str] = []
        line: list[str] = []
        line_length: int = 0

        while i < len(words):
            word: str = words[i]

            # * Greedily add as many words to the line as possible
            # * len(line) tells us how many spaces we need to add
            if line_length + len(word) + len(line) <= maxWidth:
                line.append(word)
                line_length += len(word)
                i += 1
            else:
                # * Justify the current line
                spaces = maxWidth - line_length

                if len(line) == 1:
                    # * Add all of the space to the end of the (only) word
                    result.append(line[0] + " " * spaces)
                else:
                    # * Distribute the spaces evenly
                    gaps: int = len(line) - 1  # * In ["a", "b", "c"], there are 2 gaps
                    even_space: int = spaces // gaps  # * 9 // 2 = 4 spaces per gap
                    extra: int = spaces % gaps  # * 9 % 2 = 1 extra space to leftmost

                    # * Build the final string for this line
                    parts: list[str] = []

                    for j in range(gaps):
                        # * Append the actual word
                        parts.append(line[j])

                        # * Each gap gets even_space, first j extras get +1
                        parts.append(" " * (even_space + (1 if j < extra else 0)))

                    parts.append(line[-1])
                    result.append("".join(parts))

                line = []
                line_length = 0

        # * Last line needs to be left justified (hasn't been appended yet)
        last_line = " ".join(line)
        last_line += " " * (maxWidth - len(last_line))
        result.append(last_line)

        return result


sol: Solution = Solution()
print(
    sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
)
print(sol.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
print(
    sol.fullJustify(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    )
)

print(sol.fullJustify(["Sonic"], 10))
