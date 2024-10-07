# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        def read_node(head: ListNode) :
            while head: #--> this is to read the node
                print(head.val)
                head = head.next
        
        dum = ListNode(val = None, next = head)
        # read_node(dum)

        fast, slow = dum, dum

        for _ in range(n):
            fast = fast.next # we first move fast n steps ahead
        
        while fast.next: 
            slow, fast = slow.next, fast.next # now we move both pointers until fast reaches the end of the linked list
        # read_node(slow) #[3 -> 4 -> 5]
        # read_node(fast) #[5 -> None]

        # update slow.next:
        if slow.next: 
            slow.next = slow.next. next
        # read_node(slow) # slow.ext is updated

        # read_node(dum.next)

        return dum.next



