# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        prevnext,curr=dummy,head
        for i in range(left-1):
            prevnext,curr=curr,curr.next
        prev=None
        for i in range(right-left+1):
            tmpnext=curr.next
            curr.next=prev
            prev,curr=curr,tmpnext
        prevnext.next.next=curr
        prevnext.next=prev

        return dummy.next
