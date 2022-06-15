class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # for i in l1:
        carry = 0
        root = n = ListNode()
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            a = v1 + v2 + carry
            carry = a // 10
            n.next = ListNode(a % 10)
            n = n.next
        return root.next