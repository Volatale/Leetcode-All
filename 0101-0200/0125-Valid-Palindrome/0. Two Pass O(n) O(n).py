# 125. Valid Palindrome

# * We use a two pointer approach because that allows us to simultaneously compare chars
# * There is no need to modify the string at all
# * Simply skip past any elements that are not alphanumeric
# * And whenever we find characters that ARE alphanumeric, we can call .lower()


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # copy = re.sub(r"^[a-z0-9]", "", s)
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        n: int = len(s)

        for i in range(n >> 1):
            if s[i] != s[n - i - 1]:
                return False

        return True


sol: Solution = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))

# * Time: O(n) - We have to process every character in the input in the worst case

# * Space: O(n) - In the worst case, we create a copy of the entire string
