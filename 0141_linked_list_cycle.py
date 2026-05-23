class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    # Edge case: empty list or single node
    if not head or not head.next:
        return False
    
    slow = head  # Tortoise - 1 step at a time
    fast = head  # Hare - 2 steps at a time
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # Cycle unte fast slow ni catch chestadi
        if slow == fast:
            return True
    
    # fast null ki vachindi ante cycle ledu
    return False
