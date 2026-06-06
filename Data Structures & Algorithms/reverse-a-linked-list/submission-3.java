class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;

        ListNode prev = null;
        ListNode current = head;

        // stop one step before the last node
        while (current.next != null) {
            ListNode temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }

        // handle the last node separately
        current.next = prev;
        return current; // current is now the new head
    }
}
