from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 如果无节点或只有一个节点则为回文
        if not head or not head.next:
            return True
        # 找到最中间的两个节点, 快慢指针
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 翻转后半段链表
        pre, cur = None, slow
        while cur:
            next = cur.next
            cur.next = pre
            pre, cur = cur, next
        # 逐个比较,
        while pre:
            if head.val == pre.val:
                head = head.next
                pre = pre.next
            else:
                return False
        return True


if __name__ == '__main__':
    list = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    a = Solution().isPalindrome(list)
    print(a)