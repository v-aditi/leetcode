"""
QUESTION #141 - LINKED LIST CYCLE
Difficulty: Easy
"""

# Edge case - head is None

def hasCycle(head):
    if head is None:
        return False

    pointer_one, pointer_two = head, head

    while pointer_one.next and pointer_two.next:
        if pointer_two.next.next is None:
            break
        pointer_one = pointer_one.next
        pointer_two = pointer_two.next.next

        if pointer_one == pointer_two:
            return True

    return False

"""
NOTE:
- Be careful with the order of conditionals
- Time complexity is O(N) where N = the number of nodes in the linked list
- Space complexity is O(1)

RESULTS: faster than 99.38% and memory usage less than 99.23% of submissions
"""