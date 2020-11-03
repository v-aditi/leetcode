"""
QUESTION #206 - REVERSE LINKED LIST
Difficulty: Easy
"""

# Test Case 1: 1 -> 2 -> 3 -> 4 -> 5 -> Null returns 5 -> 4 -> 3 -> 2 -> 1 -> Null
# Test Case 2: 1 -> 2 -> Null returns 2 -> 1 -> Null
# Test Case 3: 1 -> Null returns 1 -> Null
# Test Case 4: Null returns Null

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ITERATIVE APPROACH
def iterative_reverse(head):
    if head is None:
            return head

        if head.next is None:
            return head

        curr_node = head.next
        prev_node = head
        head.next = None

        while curr_node.next:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        curr_node.next = prev_node
        return curr_node

# RECURSIVE APPROACH
def recursive_reverse(head):
    if head is None:
            return head

        if head.next is None:
            return head

        curr_node = head.next
        prev_node = head
        head.next = None

        return recursive_reverse_aux(prev_node, curr_node)

def recursive_reverse_aux(prev_node, curr_node):
    if curr_node.next is None:
            curr_node.next = prev_node
            return curr_node
        else:
            next_node = curr_node.next
            curr_node.next = prev_node
            return recursive_reverse_aux(curr_node, next_node)

"""
NOTES:
- I'm getting better at coming up with test cases!

ITERATIVE APPROACH:
- Time Complexity: O(N) where N = length of the linked list
- Results: Faster than 86.81% submissions

RECURSIVE APPROACH:
- Time Complexity: O(N) where N = length of the linked list
- Results: Faster than 32.99% of submissions
"""