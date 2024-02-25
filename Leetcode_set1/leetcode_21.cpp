/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
ListNode* list3=nullptr;
ListNode* temp=nullptr;
        while(list1!=nullptr && list2!=nullptr)
        {
             if(list1->val >= list2->val)
            {
                 if(list3==nullptr)
                 {
                         list3=list2;
                         temp=list3;
                 }
                else
                {
                   temp->next=list2;
                   temp= list2;

                }
                list2=list2->next;
             
            }
           else
            {
                 if(list3==nullptr)
                 {
                         list3=list1;
                         temp=list3;
                 }
                else
                {
                   temp->next=list1;
                   temp= list1;

                }
                list1=list1->next;
             
            }
        }

        while(list1!=nullptr)
        {
            if(temp!=nullptr)
            {
             temp->next=list1;
             temp= list1;  
            }
            else
            {
                list3=list1;
                temp=list1;
            }
            list1=list1->next;
        }
        while(list2!=nullptr)
        {
            if(temp!=nullptr)
            {
             temp->next=list2;
             temp= list2;  
            }
            else
            {
                list3=list2;
                temp=list2;
            }
            list2=list2->next;
            
        }
        return list3;
        
    }
};