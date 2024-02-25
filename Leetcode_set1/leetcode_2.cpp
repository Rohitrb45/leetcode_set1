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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* l3 = nullptr;
        ListNode* temp = nullptr;
        ListNode* prev = nullptr;
        int sum = 0;
        int carry = 0;

        while (l1 != nullptr || l2 != nullptr) {
            sum = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);

            carry = sum / 10;
            sum %= 10;

            temp = new ListNode(sum);

            if (l3 == nullptr) {
                l3 = temp;
            } else {
                prev->next = temp;
            }

            prev = temp;

            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }

        if (carry > 0) {
            temp = new ListNode(carry);
            prev->next = temp;
        }

        return l3;

    }
};