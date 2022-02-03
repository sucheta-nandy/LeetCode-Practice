"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        carry = 0
        i = 0
        while curr1 or curr2 or carry != 0:
            s = carry
            if curr1:
                s += curr1.val
                curr1 = curr1.next
                
            if curr2:
                s += curr2.val
                curr2 = curr2.next
            
            if s >= 10:
                carry = s // 10
                s = s % 10
            else:
                carry = 0
                
            if i == 0:  # Just used during the first iteration to create result linked list head
                res_head = ListNode(s)
                res_curr = res_head
                i += 1
            else: 
                res_curr.next = ListNode(s)
                res_curr = res_curr.next
                   
        return res_head
