from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        lenA = 0
        lenB = 0
        curA = headA
        curB = headB
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next
        # 对齐AB两个链表
        curA = headA
        curB = headB
        if lenA > lenB:
            for _ in range(lenB, lenA):
                curA = curA.next
        if lenB > lenA:
            for _ in range(lenA, lenB):
                curB = curB.next
        while curA:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None
    def getIntersectionNode_2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        curA = headA
        curB = headB
        while curA == curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA




if __name__ == '__main__':
    listC = ListNode(8, next=ListNode(4, next=ListNode(5)))
    listA = ListNode(4, next=ListNode(1, next=listC))
    listB = ListNode(5, ListNode(6, ListNode(1, listC)))
    a = Solution().getIntersectionNode(listA, listB)
    print(a)
