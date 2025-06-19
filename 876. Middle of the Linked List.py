# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # none handling:
        if not head:
            return head # return format should be consistent.

        fast, slow = head, head
        # Fix: check both fast and fast.next are not None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # print(fast.val, slow.val)

        return slow
