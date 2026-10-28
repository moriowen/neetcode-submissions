"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # head_copy = Node(head.val, head.next, head.random)
        # curr_copy = head_copy
        # curr = head

        # while curr:
        #     new_node = Node(curr.val, curr.next, curr.random)
        #     head_copy.next = new_node
        #     curr = curr.next
        #     new_node = new_node.next

        # pass 1 - Make a map to store the new empty nodes
        # pass 2 - update the next and random pointers
        old_to_new = {None:None}
        curr = head
        
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]
        