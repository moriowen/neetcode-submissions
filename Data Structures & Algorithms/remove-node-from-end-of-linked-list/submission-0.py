# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1

        index_to_delete = count - n
        curr = head

        if index_to_delete == 0:
            return head.next

        while index_to_delete-1:
            index_to_delete -= 1
            curr = curr.next
        
        curr.next = curr.next.next

        return head
