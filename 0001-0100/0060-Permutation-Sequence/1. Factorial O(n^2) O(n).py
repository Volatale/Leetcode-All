# 60. Permutation Sequence


# * There are (n-1)! blocks of permutations that share the same first number
# * So each block size has size (n-1)!
# * We can think of `k` as pointing into one of these blocks
# * If we want the `kth` permutation:
# *     - Divide (k-1) by (n-1)! to know which block to target
# *     - The quotient = index of first digit
# *     - The remainder = where you are inside that block
# * So at each step, `k` tells you which choice of digit and then we reduce the problem size
# ! There is a recursive pattern here
# * Once we fix the first digit, the problem is reduced from "find k-th perm of n digits"
# * To "find some smaller k-th perm of n-1 digits"
# ! The quotients we compute are factorial digits
# *     - The 1st choice is in base (n-1)!
# *     - The 2nd choice is in base (n-2)!
# *     - The 3rd choice is in base (n-3)!
# * we are converting (k - 1) into a "factorial number system" representation
# *     - Then we map those digits into choices of numbers
# * Dividing by fact gives you which block k falls into
# *     - That’s how you pick the digit
# * Modding by fact tells you where you are inside that block
# *     - That’s your new k for the smaller subproblem
# ! It is similar to how we use the following in base 10 arithmetic:
# *     - quotient = k // base
# *     - remainder = k % base
# ! This can be thought of as rows and columns
# *     - The permutation space is structured as a grid of factorial-sized blocks
# !     - However, instead of each group having a fixed size, the group sizes shrink each step
# *         - If n = 4, then 24
# *         - If n = 3, then 6
# *         - If n = 2, then 2
# *         - If n = 1, then 1..
# *     - Hence the term "factorial number system"


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial

        nums: list[str] = [str(i) for i in range(1, n + 1)]  # * Digits available
        k -= 1  # * Convert to 0-indexed
        result: list[str] = []

        # * We are dealing with permutation blocks of size (n-1)! -> (n-2)! etc
        # * if n = 4, then there are 6 (4-1)! permutations in a row starting with 1
        # * Then 6 in a row starting with 2 etc. When n = 3, we have blocks of size 2 (3-1)!
        for i in range(n, 0, -1):
            block_size = factorial(i - 1)  # * No. of Perms in each block
            index = k // block_size  # * The number we choose
            k = k % block_size  # * Group size shrinks in the next iteration
            result.append(nums.pop(index))  # * Remove this number from the choices

        return "".join(result)


sol: Solution = Solution()
print(sol.getPermutation(1, 1))  # * "1"
print(sol.getPermutation(2, 2))  # * "21"
print(sol.getPermutation(2, 3))  # * "12"
print(sol.getPermutation(3, 4))  # * "231"
print(sol.getPermutation(4, 2))  # * "1243"
print(sol.getPermutation(4, 3))  # * "1324"
print(sol.getPermutation(4, 4))  # * "4123"

# * Time: O(n^2) - It takes O(n) to generate the list of numbers
# * Then, we perform an O(n) loop, and within each iteration, we compute a factorial
# * The time complexity of factorial is O(n), so we get O(n * n)

# * Space: O(n) - The size of the list of numbers to choose is `n`, as is the return string
