# 2. Add Two Numbers

# * We are given two non-empty linked lists that represent (non-negative) integers
# *     - The digits are stored in reverse order
# *     - Each node represents a single digit [0, 9]
# * Our goal is to return the sum of both linked lists and return it
# !     - Our return value is a linked list in and of itself
# * Since we always have two linked lists, we can use a two pointer approach
# * Specifically, we are given two SINGLY linked lists, so we can ONLY iterate forward
# ! Mathematically, since we are dealing with addition, we'll have to deal with overflows
# *     - In other words, place value is a relevant concept and we need to be able to handle those cases
# ! Since we need to return a linked list, we should use the "dummy node" technique to avoid edge cases


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode:
        dummy: ListNode = ListNode(-1)  # To attach the first node to
        curr: ListNode = dummy

        # Two pointers used to iterate over the linked lists
        left = l1
        right = l2

        # Used to handle overflows in place value (a + b > 9)
        carry: int = 0

        while left or right or carry:
            # Start with the carry
            sum = carry

            if left:
                sum += left.val
                left = left.next  # Move to the next

            if right:
                sum += right.val
                right = right.next

            # We use the modulus operator to get the "remainder" of the addition (place value column)
            # 9 + 4 = 13, so we know the NEXT column should have an extra ten added to it (1 ten = 10 ones)
            carry = sum // 10
            curr.next = ListNode(sum % 10)

        return dummy.next


# Time: O(n) - It takes O(n) to iterate through both input lists, where `n` is the longest of the two
# Creating new noeds takes O(1) time

# Space: O(n) - In the worst case, there are `n` nodes created
# the return list's size scales with the length of the longest input
