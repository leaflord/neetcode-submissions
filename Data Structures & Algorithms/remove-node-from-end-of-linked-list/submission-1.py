
class Solution:
    def removeNthFromEnd(self, head, n: int):
        res = ListNode(-1, head)
        fast = head
        slow = head
        i = 1
        while fast:
            if i > n:
                slow = slow.next
            fast = fast.next
            i += 1

        curr = res
        while curr:
            if curr.next is slow:
                curr.next = curr.next.next
                break
            curr = curr.next
        return res.next