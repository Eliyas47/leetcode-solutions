class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next     # Save next node
            curr.next = prev    # Reverse pointer
            prev = curr         # Move prev forward
            curr = nxt          # Move curr forward

        return prev
