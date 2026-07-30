# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, prev, curr = None, None, None
        while list1 or list2:
            if (not list2 and list1) or (list1 and list2 and (list1.val <= list2.val)):
                curr = list1
                list1 = list1.next
            else:
                curr = list2
                list2 = list2.next
            curr.next = None
            if not head:
                head = curr
            else:
                prev.next = curr
            prev = curr
        return head