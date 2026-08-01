# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 1
        if not head or not head.next or k ==0:
            return head
        pt1 = head
        while pt1.next is not None:
            pt1 = pt1.next
            length +=1
        k = k%length
        if k == 0:
            return head
        steps_to_tail = length - k-1
        pt2 = head
        for _ in range(steps_to_tail):
            pt2 = pt2.next
        new_head = pt2.next
        pt2.next = None
        pt1.next = head
        return new_head
