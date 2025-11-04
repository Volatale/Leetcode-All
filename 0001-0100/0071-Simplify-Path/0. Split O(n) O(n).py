# 71. Simplify Path

# * The goal is to simplify the path to create a "valid" path string
# * We have to contend with a few possible characters
# *     "/", which is used as a delimiter between directories
# *     ".." which means "go back to the previous directory"
# *     More than 2 dots is a valid file name or directory name
# *     Single dots represent the current directory, and should be removed
# *     Any other string is a directory name
# *     Multiple slashes are treated the same as a single slash
# ! We can handle this by splitting the array via "/"
# * That would give us an array of everything except the slashes
# ! The path can be simulated using a stack
# * If we encounter a "..", pop the stack (because we go back to the previous directory)
# * If we encounter a word, push it to the stack
# ! At the very end, we join the array using the "/" delimiter (to create a string)
# * And we also append a "/" at the very start of the array


class Solution:
    def simplifyPath(self, path: str) -> str:
        # * Split the string by "/" to remove them all
        strings: list[str] = path.split("/")

        # * Represents the final simplified path
        canonical_path: list[str] = []

        for s in strings:
            if s == ".." and canonical_path:
                # * Go back up one directory
                canonical_path.pop()
            elif s != "." and s != ".." and s != "":
                # * Append anything else to the path (it is valid)
                canonical_path.append(s)

        return "/" + "/".join(canonical_path)


sol: Solution = Solution()
print(sol.simplifyPath("/home/"))
print(sol.simplifyPath("/"))
print(sol.simplifyPath("/home//foo/"))
print(sol.simplifyPath("/home/user/Documents/../Pictures"))
print(sol.simplifyPath("/../"))
print(sol.simplifyPath("/.../a/../b/c/../d/./"))
