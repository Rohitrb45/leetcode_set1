class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def rotateRight( head, k):
        if not head:
            return None

        tail = head
        lenList = 1
        while tail.next:
            tail = tail.next
            lenList += 1

        k = k%lenList
        print("k=",k)
        if k == 0:
            return head

        newTail = head
        print("lenlist=",lenList-k-1)
        for i in range(lenList-k-1):
            print("inside",i)
            newTail = newTail.next
        
        newHead = newTail.next
        print("nh",newHead.val)
        print("nt",newTail.val)        
        newTail.next = None
        tail.next = head
        return newHead
a=ListNode(0)
b=ListNode(1)
c=ListNode(2)
a.next=b
b.next=c
m=rotateRight( a, 2000000000)
while(m):
     print(m.val)
     m=m.next