class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        next, reversed = head.next, self.reverseList(head.next)
        head.next, next.next = None, head # we don't know where the rest of list is, but we know it's the same node
        return reversed