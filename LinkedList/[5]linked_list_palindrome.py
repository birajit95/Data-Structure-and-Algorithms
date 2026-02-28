"""
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a or false otherwise.

 
"""


class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # Step 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # Step 3: Compare halves
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True