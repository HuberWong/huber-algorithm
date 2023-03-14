from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head  # 链表只由一个元素使可以直接返回



if __name__ == '__main__':
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    Solution().deleteDuplicates(head=head)
    Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2))))
    print()
