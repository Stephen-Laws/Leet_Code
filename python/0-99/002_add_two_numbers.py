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
        l1_val = self.getVal(l1)
        l2_val = self.getVal(l2)
        res = l1_val+l2_val
        head = node = ListNode(0)
        for digit in reversed(str(res)):
            d = int(digit)
            node.next = ListNode(d)
            node = node.next
            print(head.next)
        
        return head.next
            
        def getVal(self, l):
            val = l.val
            exp = 10
            while l.next != None:
                l = l.next
                val += l.val*exp
                exp*= 10
            return val