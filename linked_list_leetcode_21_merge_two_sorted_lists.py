# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 is not None else list2
        return dummy.next


if __name__ == '__main__':
    list1 = ListNode(val=1, next=ListNode(2, ListNode(4)))
    list2 = ListNode(val=1, next=ListNode(3, ListNode(4)))
    Solution().mergeTwoLists(list1, list2)
    list2 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(4)
