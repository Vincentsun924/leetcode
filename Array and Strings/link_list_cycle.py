# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        turtle = head
        hare = head

        #hare moves twice as fast as turtle
        while hare and hare.next:
            turtle.next
            hare.next.next
            #if there is a cycle then hare will lap turtle eventually 
            if turtle == hare:
                return True
            
        return False