/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        if(head == NULL || head->next == NULL) { //空链或只有一个结点
            return head; //直接返回头指针
        } else { //有两个以上结点
            ListNode* newHead = reverseList(head->next); //反转以第二个结点为头结点的子链表
            head->next->next = head; //将之前的头结点连接到子链尾
            head->next = NULL; //head->next指向最后一个结点
            return newHead;
        }
    }
};
