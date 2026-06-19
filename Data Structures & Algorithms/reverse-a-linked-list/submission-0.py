# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        temp_tail = head
        temp = head.next
        temp_tail.next = None

        while temp is not None:
            next_node = temp.next
            temp.next = temp_tail
            temp_tail = temp
            temp = next_node
        return temp_tail