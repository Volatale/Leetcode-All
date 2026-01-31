# 161. One Edit Distance

# * It is possible that len(s) != len(t), but we want to ensure that len(s) >= len(t)
# * Why? Because that enables us to solely focus on `delete` and `replace` operations instead of the additional `insert`
# * Since len(s) >= len(t), we can't insert any characters as this would not get us closer to the goal
# * If the string lengths differ by more than 1, then no matter what we do, s will never equal t
# *     - We are only allowed to perform a SINGLE operation - not multiple
# * If s[i] == t[i], then we don't do anything, just progress; no operations need to be performed here
# * Otherwise, we know s[i] != t[i] so we need to do something about it
# * If (n == m), then we know the lengths of the strings is equal
# !     - This means we CANNOT delete a character, as deleting a character would result in len(s) < len(t)
# *       And we are not able to insert a character to replace it (as we only have 1 operation max)
# *     - Thus, we are left with our only option being replace the current character
# *     - After the replacement, s[i] == t[i], so we simply need to compare the REST of the strings
# *         - We already made our operation and we aren't allowed to perform multiple so we've done all we can
# * If (n != m), then we know the lengths of the strings is NOT equal
# !     - This means we CANNOT simply replace a character, even if we did, we wouldn't be any closer to the goal
# *     - Therefore, our only option is to delete the current character
# *       We already know that `n` has one more character at this point, so removing it equalizes the lengths
# *     - Note that we didn't actually "use" the current character in `t`, so we compare s[i+1:] and t[i:], and not t[i+1:]
# *       We haven't yet validated that s[i+1] == t[i]
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # * By ensuring s < t we only have to consider deletions and not both insert/deletion
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)

        n: int = len(s)
        m: int = len(t)

        # * We'd have to remove more than 1 character
        if n - m > 1:
            return False

        for i in range(n):
            if s[i] != t[i] and n == m:
                return s[i + 1 :] == t[i + 1 :]  # * Replace the character
            elif s[i] != t[i] and n != m:
                return s[i + 1 :] == t[i]  # * Delete the character

        # * We know the chars are equal (except the last), so we just remove it
        return n - 1 == m


# * Time: O(n) - We always perform `n` iterations regardless of input size
# * If abs(len(s) - len(t)) > 1, then there are no iterations at all

# * Space: O(n) - Lets say the inputs were both length 100 and s[0] != t[0]
# * In this case, we end up creating a substring for both s and t of the length (100 - 1), which scales with `n`
