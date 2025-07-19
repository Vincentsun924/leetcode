# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # list_link = []
        # current = head
        # while current:
        #     list_link.append(current)
        #     current = current.next

        # print(list_link)
        # return list_link[len(list_link) //2 ]


#or    
        #initilze both counter at the first index
        mid = head
        last = head

        #since last is growing twice as fast, mid will be in the middle, if there is a possible move for next, the next will move and mid will move, if there is no possible move for next, then next will stop and return mid
        while last and last.next:
            mid = mid.next
            last = last.next.next

        
        return mid
