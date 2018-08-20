# TAGS: linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=head
        while temp and temp.next:
            temp.val, temp.next.val = temp.next.val, temp.val
            temp=temp.next.next
        return head