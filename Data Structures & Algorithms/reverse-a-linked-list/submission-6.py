class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        reversed, head.next.next, head.next = self.reverseList(head.next), head, None
        return reversed