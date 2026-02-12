# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Dummy node to simplify insertion at head
        dummy = ListNode(0)
        curr = head

        while curr:
            # At each iteration, we insert curr into the sorted part
            prev = dummy
            # Find the right place to insert curr
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Save next node before re-linking
            next_temp = curr.next

            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            # Move to the next node
            curr = next_temp

        return dummy.next
