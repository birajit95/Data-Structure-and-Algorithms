
"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head is None:
            return 
        prev = None
        cur = head


        while cur.next is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        cur.next = prev

        head = cur

        return head
        
        