# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_1 = []
        curr_1 = l1
        while curr_1:         
            list_1.append(curr_1.val)
            curr_1 = curr_1.next
        list_2 = []
        curr_2 = l2
        while curr_2:
            list_2.append(curr_2.val)
            curr_2 = curr_2.next

        num_1 = int(''.join(map(str, list_1[::-1])))
        num_2 = int(''.join(map(str, list_2[::-1])))
        result = num_1+num_2
        reversed_result_list = [int(d) for d in str(result)][::-1]
        dummy = ListNode(0)
        curr = dummy
        for digit in reversed_result_list:
            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next
        
        