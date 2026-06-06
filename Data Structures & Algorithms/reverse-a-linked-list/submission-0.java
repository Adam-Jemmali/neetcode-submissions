/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {

        // 1(current_---> 2(next11---> ---> 4

        // null   --< 1(prev       2(next1=current)
        
        ListNode prev=null;
        ListNode current=head;

        while( current!= null){

            ListNode next1=current.next;

            current.next= prev;
            prev=current; //place ccurrent as prev
            current=next1;
            
        }
        return prev;
    }
}
