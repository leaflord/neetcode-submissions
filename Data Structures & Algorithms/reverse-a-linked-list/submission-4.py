class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        next = head.next
        reversed = self.reverseList(next)
        next.next = head # we don't know where the rest of list is, but we know it's the same node
        head.next = None
        return reversed