# 151. Reverse Words in a String

# * We can use a two pointer approach where where we find the boundaries of each word (starting from the right)
# * Then, we can simply take the substring from s[left+1:right+1] and push that to the results array
# * Naturally, we need to skip over any whitespace; instead of having it be implicit with each word...
# * We can resort to appending the whitespace ourselves
# * If the length of the results array > 0, then we need to append some whitespace
class Solution:
    def reverseWords(self, s: str) -> str:
        result: list[str] = []
        n: int = len(s)
        # * Iterate backwards to avoid reversing
        right: int = n - 1

        while right >= 0:
            # * Skip all of the trailing whitespace
            while right >= 0 and s[right] == " ":
                right -= 1

            # * Perform a bounds check
            if right < 0:
                break

            # * Used to find the start of this word
            left: int = right

            # * Move left to the index one before the start of this word
            while left >= 0 and s[left] != " ":
                left -= 1

            # * Process the word and add whitespace if necessary
            if len(result) > 0:
                result.append(" ")

            result.append(s[left + 1 : right + 1])
            right = left

        return "".join(result)


sol: Solution = Solution()
print(sol.reverseWords("the sky is blue"))
print(sol.reverseWords("  hello world  "))
print(sol.reverseWords("a good   example"))

sonic: str = "sonic"
print("".join(reversed(sonic)))

# * Time: O(n) - We have to iterate over every character in the input, so the time taken scales linearly with `n`

# * Space: O(n) - We are using Python, so we cannot mutate strings in-place
# * Thus, we must resort to using a separate array for the output
