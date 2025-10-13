class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        curr = head
        while curr: 
            nodes.append(curr)
            curr = curr.next 
        
        l = 0
        r = len(nodes)-1
        while l < r:
            nodes[l].next = nodes[r]
            l += 1 
            if l >= r: 
                break
            nodes[r].next = nodes[l]
            r -= 1
        nodes[l].next = None 