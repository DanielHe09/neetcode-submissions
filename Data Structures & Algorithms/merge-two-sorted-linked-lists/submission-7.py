class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = list1
        curr1 = list1
        prev1 = None
        curr2 = list2

        if list1 is None:
            return list2
        while curr1 != None and curr2 != None:

            if curr2.val<=curr1.val:
                temp = curr2.next
                curr2.next = curr1
                if (prev1!=None):
                    prev1.next = curr2
                if (curr1==head): head = curr2
                prev1 = curr2
                curr2 = temp

            else:
                prev1 = curr1
                curr1 = curr1.next

                

        if curr2 != None:
            prev1.next = curr2
              

        return head