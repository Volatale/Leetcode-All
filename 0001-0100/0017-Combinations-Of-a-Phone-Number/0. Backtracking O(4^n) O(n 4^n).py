# 17. Combinations of a Phone Number

# * We are given string containing digits from 2-9
# *     - The goal is to return all possible combinations it can represent
# * The digits map to the same letters they would map to on a telephone
# *       2 -> abc
# *       3 -> def
# *       etc,
# * Since this is a combinations problem, we need to take each digit and form an output
# * Naturally, this is recursive since we are working digit-by-digit
# * At each level of recursion, we get all of the characters that the digit maps to
# * Then, we append each of those characters to the current string (that exists at this level)
# *
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        mapping: dict[str, tuple[str, ...]] = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }

        return self._backtrack(0, digits, mapping, "", [])

    def _backtrack(
        self,
        i: int,
        digits: str,
        mapping: dict[str, tuple[str, ...]],
        curr: str,
        results: list[str],
    ) -> list[str]:
        # * Base Case (no more characters)
        if i == len(digits):
            results.append(curr)  # * Add the finished combination
            return results

        # * Get all of the characters
        chars: tuple[str, ...] = mapping[digits[i]]

        # * Iterate through each character in the tuple and append it to "curr"
        for char in chars:
            self._backtrack(i + 1, digits, mapping, curr + char, results)

        return results


sol: Solution = Solution()
print(sol.letterCombinations("22"))
print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))
print(sol.letterCombinations("2"))
print(sol.letterCombinations("79"))

# * Time: O(4^n) - In the worst case, for each character in `digits`, there are 4 calls to `_backtrack()`
# * The depth of the recursion is O(n) because there are 4 levels of recursion

# * Space: O(n * 4^n) - The depth of the recursion scales with the length of the input
# * Additionally, the size of the returned list scales with the length of the input (and the digits themselves)
# * The total number of results is 4^n in the worst case, and each string has length `n`
# * So the total memory used scales at a rate of O(n * 4^n) (assuming we're also counting the output storage)
