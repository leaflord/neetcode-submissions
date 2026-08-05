class Solution:
    def removeNthFromEnd(self, head, n: int):
        res = ListNode(-1, head)
        fast = head
        slow = res
        i = 1
        while fast:
            if i > n:
                slow = slow.next
            fast = fast.next
            i += 1
        slow.next = slow.next.next
        return res.next