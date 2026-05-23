class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    # Fast & Slow pointers start at head
    slow = head
    fast = head
    
    # Fast 2 steps, slow 1 step
    # Fast null ki or last node ki velthe slow middle lo untadi
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
