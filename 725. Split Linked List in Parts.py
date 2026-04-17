class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Count total nodes
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Step 2: Determine size of each part
        base_size, extra = divmod(length, k)
        
        result = []
        curr = head
        
        for i in range(k):
            part_head = curr
            size = base_size + (1 if i < extra else 0)
            
            # Step 3: Traverse size-1 nodes, then cut
            for j in range(size - 1):
                if curr:
                    curr = curr.next
            
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            
            result.append(part_head)
        
        return result
