# * 157. Read N Characters Given Read4


class Solution:
    def read(self, buf: list[str], n: int) -> int:
        chars_copied: int = 0
        chars_read: int = 4  # * Initialized to 4 so we can start the while loop
        temp_buf: list[str] = [""] * 4

        while chars_read == 4:
            chars_read = self.read4(temp_buf)

            # * Copy the characters from the temp buffer to the non-temp
            for i in range(chars_read):
                # * There are no more characters to read
                if chars_copied >= n:
                    return n

                buf[chars_copied] = temp_buf[i]
                chars_copied += 1

        # * It is possible that there weren't `n` characters to copy
        return min(chars_copied, n)

    def read4(self, buffer: list[str]) -> int: ...


# * Time: O(n) - In the worst case, we have to read all `n` characters

# * Space: O(n) - It is possible we have to create a copy of all `n` characters
