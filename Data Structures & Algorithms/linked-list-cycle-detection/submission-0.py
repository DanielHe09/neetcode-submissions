# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #if there is a cycle there is no end to the linked list
        fast=head
        slow=head

        while fast and slow:
            slow = slow.next
            fast = fast.next
            if fast == None: break
            else: fast = fast.next

            if (slow is fast): return True 
        
        return False
