/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    /*if(head==0 || head->next==0)
    {
        return 0;
    }*/
    if (head->next == NULL) {
        return head->next;
    }
    
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    
    while (n--) {
        fast = fast->next;
    }
    
    if (fast != NULL) {
        while (fast->next != NULL) {
            slow = slow->next;
            fast = fast->next;
        }
        slow->next = slow->next->next;
    }
    else {
        slow->val = slow->next->val;
        slow->next = slow->next->next;
    }
    
    return head;
    /* struct ListNode* dummy=(struct ListNode *)malloc(2*sizeof(struct ListNode*));
    dummy->val=0;
    dummy->next=head;
    struct ListNode* temp=head;
    struct ListNode* temp1=0;
    int len=0;
    while(temp!=0)
    {
        temp=temp->next;
        len+=1 ;
    }
     printf("len=%d\n",len);
    temp=head;
    int k=0;
    if (n==len)
    {
          k=len-2;
    }
    else
    {
        k=len-n-1;
    }
    printf("k=%d",k);
    while(k!=0)
    {
        temp=temp->next;
        k--;
    }
    printf("node_val=%d",temp->val);
    
    if(temp->next!=0 and n!=len)
    {
      temp1=temp->next;
      temp->next=temp1->next;
      free(temp1);
    }
    else
    {
         temp1=
    }

    return dummy->next;
    */
}