
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list1, tail1, list2, _ = self.split(head)
        tail1.next = None
        list2 = self.reverseList(list2) # tail2 is last anyway
        self.alternate(list1, list2)

    def alternate(self, list1, list2):
        while list1 and list2:
            next2 = list2.next
            next1 = list1.next
            list1.next = list2
            list1.next.next = next1
            list2 = next2
            list1 = next1

    def reverseList(self, head: Optional[ListNode]):
        if not head or not head.next:
            return head
        next = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return next

    def split(self, head: ListNode | None):
        slow = fast = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            prev = slow
            slow = slow.next
        return head, prev, slow, fast