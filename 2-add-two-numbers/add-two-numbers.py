# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Continue looping if there's still a node in l1, l2, or a remaining carry
        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if we've reached the end of a list
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the resulting digit (total % 10)
            current.next = ListNode(total % 10)
            
            # Move the pointers forward
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # The result list starts at the node right after our dummy
        return dummy.next