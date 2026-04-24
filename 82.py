# Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next