# Given the head of a linked list, return the list after sorting it in ascending order.

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while head:
            heapq.heappush(ans,head.val)
            head = head.next
        newhead = ListNode()
        prev = newhead
        while ans:
            prev.next = ListNode(heapq.heappop(ans))
            prev = prev.next
        return newhead.next
