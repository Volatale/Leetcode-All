# 28. Find the Indexof the First Occurrence in a String

# * We can simply use the Rabin-Karp Algorithm here
# * Rabin-Karp is essentially a rolling hash implementation
# * Rolling hashes are conceptualy similar to number bases, with a few differences
# * We have some constants to contend with
# *     - base: Essentially a number base (except that base is PRIME)
# *     - k: The length of the pattern
# *     - MOD: An extremely large prime number
# * The algorithm works as follows:
# * Compute the initial length k hashes for both "haystack" and "needle"
# *     - H = (s[i] * base^(k - 1)) + (s[i + 1] * base^(k - 2)) + ... + (s[i + k - 1] * base^(k-k))
# ! Notice that instead of computing powers repeatedly, we precompute the powers of base
# * Since we already have a `k` length window, we immediately check if we have a match
# ! We are working with hashes, there is always the potential for hash collisions
# * Handling the sliding window:
# * The LEFTMOST character's weight is removed from the window
# *     - That character was added using: (s[i-k] * base^(k-1))
# *     - Therefore, we SUBTRACT that value from the hash value
# ! Since we are subtracting, there is a chance that the result is negative
# *     - To deal with this case, we ADD `MOD` to the result
# *     - After this, we modulo by `MOD` to avoid overflows
# * Now we have: (s[i + 1] * base^(k-2)) + (s[i + 2] * base^(k-3)) + ... + (s[i + k - 1] * base^(k-k))
# ! Thus, every exponent is now 1 less than it should be
# * To add the next value to the window we use the following formula:
# *     - H = (H * base + s[i + k])
# !     - Since all of the exponents are 1 less, we multiply by base to fix the weights

# * In a more simple example, imagine we have the following values/constants:
# *       a = 1, b = 2, c = 3 ... z = 26
# *       base = 10, `s` = "abcdef", `p` = "abc"
# * H = (1 * 100) + (2 * 10) + (3 * 1) = 123
# * Then, we need to remove the leftmost weight from the window (a)
# *     - H' = (2 * 10) + (3 * 1) = 23
# ! The hash value should be 234 at the end of all of this, and we currently have 23
# *     - Thus, we multiply by 10 (remember, this is our BASE)
# *     - 23 * 10 = 230
# * Finally, we add the new value (s[i + k])
# *     - 230 + 4 = 234 (the new and correct hash value)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # * The "needle" cannot possibly exist within the "haystack"
        if len(needle) > len(haystack):
            return -1

        # * Constants for computation
        base: int = 31
        k: int = len(needle)
        MOD: int = 10**9 + 7

        # * Precompute the powers of base
        powers: list[int] = [1] * k
        for i in range(1, k):
            powers[i] = (powers[i - 1] * base) % MOD

        # * Compute hash values for both "haystack" and "needle"
        p_hash: int = 0
        s_hash: int = 0

        # * Find the needle in the haystack
        for i in range(k):
            val_p: int = ord(needle[i]) - 96
            val_s: int = ord(haystack[i]) - 96
            p_hash = (p_hash + val_p * powers[k - i - 1]) % MOD
            s_hash = (s_hash + val_s * powers[k - i - 1]) % MOD

        for i in range(len(haystack) - k + 1):
            if s_hash == p_hash and haystack[i : i + k] == needle:
                return i

            # * Slide the window: remove left char, add the current char
            if i + k < len(haystack):
                removed_val = ((ord(haystack[i]) - 96) * powers[k - 1]) % MOD
                s_hash = (s_hash - removed_val + MOD) % MOD
                s_hash = (s_hash * base + (ord(haystack[i + k]) - 96)) % MOD

        # * The needle was not found in the haystack
        return -1


sol: Solution = Solution()
print(sol.strStr("sadbutsad", "sad"))  # * 0
print(sol.strStr("leetcode", "leeto"))  # * -1
print(sol.strStr("silver sonic shadow", "sonic"))  # * 7

# * Time: O(n + k) - It takes O(k) to precompute powers, and O(k) for the initial hash
# * For the sliding window portion, we slide (n - k + 1) times, so approximately `n`
# * Thus, the expected time complexity is O(n + k), and in the worst case it is O(nk) (lots of collisions)

# * Space: O(k) - We need O(k) space to store the precomputed powers
