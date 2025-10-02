# 38. Count and Say

# * The goal is to take an int input `n` and return a string based on that value
# * We need to return the "run-length encoding" (RLE) of the current string
# *     - `countAndSay(1)` = ""
# *     - `countAndSay(2)` = "11"
# *     - `countAndSay(3)` = "21"
# *     - `countAndSay(4)` = "1211"
# *     - `countAndSay(5)` = "111221"
# *     - `countAndSay(6)` = "312211"
# * We count the number of identical consecutive digits there are, and append that to a new string
# * Then, we say what the digit was
# * So something like "312211" translates to (in English):
# *     - 3 Ones, 2 Twos, 2 Ones


class Solution:
    def countAndSay(self, n: int) -> str:
        # * Immediately hit the base case
        if n == 1:
            return "1"

        RLE: str = "1"

        # * Generate terms from 2 up to n
        for _ in range(1, n):
            new_RLE: list[str] = []
            count: int = 1

            # * Go through the current string
            for i in range(1, len(RLE)):
                if RLE[i] == RLE[i - 1]:
                    count += 1
                else:
                    # * Add `count`` and the digit itself to new_RLE
                    new_RLE.append(str(count))
                    new_RLE.append(RLE[i - 1])
                    count = 1  # * Reset the count

            # * Append the final group
            new_RLE.append(str(count))
            new_RLE.append(RLE[-1])

            # * Prepare for next iteration
            RLE = "".join(new_RLE)

        return RLE


sol: Solution = Solution()
print(sol.countAndSay(0))  # * ""
print(sol.countAndSay(1))  # * "1"
print(sol.countAndSay(2))  # * "11"
print(sol.countAndSay(3))  # * "21"
print(sol.countAndSay(4))  # * "1211"
print(sol.countAndSay(5))  # * "111221"
print(sol.countAndSay(6))  # * "312211"

# * Time: O(Ln) - Each call processes the entire current string once (O(Ln))

# * Space: O(Ln) - String space
