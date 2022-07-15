# https://oj.leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
     
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        loop = False
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                loop = True
                break
                
        if loop:
            while slow != head:
                slow, head = slow.next, head.next 
            return head
        return None

        
    def detectCycleslow(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lists = []
        foundloop = False
        while head:
            if head in lists:
                return head
            else:
                lists.append(head)
            head = head.next
        return None
            