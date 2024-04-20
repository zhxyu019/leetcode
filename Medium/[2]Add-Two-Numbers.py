# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:
            sum_val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum_val // 10
            sum_val %= 10
            current.next = ListNode(sum_val)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next