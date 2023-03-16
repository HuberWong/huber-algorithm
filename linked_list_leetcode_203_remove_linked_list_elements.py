from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                 cur.next = cur.next.next
            else:
                cur = cur.next
        return head

if __name__ == '__main__':
    # list = ListNode(1,ListNode(2,ListNode(6,ListNode(3,ListNode(4,ListNode(5,ListNode(6)))))))
    # a = Solution().removeElements(list, 6)

    list = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    a = Solution().removeElements(list, 7)
    print(a)
