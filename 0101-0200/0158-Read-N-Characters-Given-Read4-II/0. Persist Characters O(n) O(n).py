# 158. Read N Characters Given read4 II - Call Multiple Times

# * Since `read` can be called multiple times, it is possible that we read "too many" characters
# * We didn't need them then, but we couldn't exactly get rid of those characters
# *     - Why? Because we aren't allowed to make the "file pointer" (or, our stand-in) go backwards
# * The extra characters we have musst be able to persist across calls
# * Thus, the easiest way to handle this is to use instance variables
# ! Since we know `read4` aims to read 4 characters (or less), that poses a problem
# * What if we still have a character in `temp_buf` (from last call), but we still want to read 4 "new" characters?
# ! If there are characters leftover, we should use them immediately
# * Only when all of the leftover characters have been used should we aim to read more
# *     - This ensures we don't waste any characters
class Solution:
    def __init__(self):
        self.temp_buf: list[str] = [""] * 4
        self.buffer_index: int = 0  # * Current index in buffer
        self.buffer_size: int = 0  # * No. of valid chars in buffer

    def read(self, buf: list[str], n: int) -> int:
        chars_read: int = 0

        while chars_read < n:
            # * Only consume more chars if we have expended the internal buffer
            if self.buffer_index == self.buffer_size:
                self.buffer_size = self.read4(self.temp_buf)
                self.buffer_index = 0

                # * If read4 returns 0, there are no more chars
                if self.buffer_size == 0:
                    break

            # * Copy characters from internal buffer to output buffer
            while chars_read < n and self.buffer_index < self.buffer_size:
                buf[chars_read] = self.temp_buf[self.buffer_index]
                self.buffer_index += 1
                chars_read += 1

        return chars_read

    def read4(self, buf: list[str]) -> int: ...


# * Time: O(n) - We need to read `n` characters in the "worst" case

# * Space: O(n) - The output array `buf` will contain `n` characters in the worst case
