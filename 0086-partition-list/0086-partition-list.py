# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_d = ListNode(0)
        great_d = ListNode(0)
        less = less_d
        great = great_d
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
                curr = curr.next
            elif curr.val >= x:
                great.next = curr
                great = great.next
                curr = curr.next
        less.next = great_d.next
        great.next = None
        return less_d.next
