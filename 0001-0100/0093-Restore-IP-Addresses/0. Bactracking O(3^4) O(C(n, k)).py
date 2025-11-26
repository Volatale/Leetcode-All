# 93. Restore IP Addresses

# * Each integer in an IP address is at most 3 digits
# * There are 4 integers in a single IP address
# * Thus, there are 3 dots separating these IP addresses
# * Therefore, we can say that the depth of recursion is at most 4
# *     - Any greater implies we have more than 4 numbers
# * At each level of recursion, there are 3 possible split points
# *     - Why? Because each (valid) integer can be 3 digits long at most
# *     - So we need to try all three possibilities at each step
# * All of the numbers must be in the range 0 <= num <= 255
# * Additionally, numbers must not contain leading zeroes
# *     - To check for this case, we can get the length of the current substring
# *     - Then, if the length is > 1, and the 0th character is a 0, we have a leading zero


class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def backtrack(start: int, depth: int):
            # * Base Case: The depth should not be greater than 4
            if depth > 4:
                return

            # * Base Case: There are 4 numbers, and we used every digit
            if depth == 4 and start == n:
                results.append(".".join(path))
                return

            # * There are 3 possible "split" points at each level of recursion
            for i in range(start, min(n, start + 3)):
                ss = s[start : i + 1]

                # * Numbers must be: 0 <= num <= 255, and cannot have leading zeroes
                if int(ss) > 255 or (len(ss) > 1 and ss[0] == "0"):
                    continue

                path.append(ss)  # * Choose
                backtrack(i + 1, depth + 1)  # * Explore
                path.pop()  # * Un-choose

        # * If there are more than 12 digits, we can't make an IP address
        if len(s) > 12:
            return []

        n: int = len(s)
        results: list[str] = []
        path: list[str] = []
        backtrack(0, 0)
        return results


sol: Solution = Solution()
print(sol.restoreIpAddresses("25525511135"))
print(sol.restoreIpAddresses("0000"))
print(sol.restoreIpAddresses("101023"))

# * Time: O(3^4) - Each call can lead to 3 additional calls
# * Thus the branching factor is 3
# * The depth of the recursion is 4 since we can only create 4 numbers

# * Space: O(C(n, k)) - An IP address has a maximum length of 15
# * There can only be C(n, k) valid combinations (most will fail)
# * In this case, "k" is 4, so the results array scales at a rate of O(C(n, k))
# * The depth of the recursion is O(4) (constant)
