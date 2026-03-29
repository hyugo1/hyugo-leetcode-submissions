# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        secondhalf = slow.next
        prev = slow.next = None
        while secondhalf:
            tmp = secondhalf.next
            secondhalf.next = prev
            prev = secondhalf
            secondhalf = tmp
        
        first, secondhalf = head, prev

        while secondhalf:
            tmp1, tmp2 = first.next, secondhalf.next
            first.next = secondhalf
            secondhalf.next = tmp1
            first = tmp1
            secondhalf = tmp2
            
