"""
input            : 1->2->3->4->5->None
expected output  : 5->4->3->2->1->None

Atleast a node is guaranteed to be there with value
"""


def reverse_linked_list(head):
    prev = None
    cur = head
    print("cc vsl")
    while head:
        print("cc")
        nex = head.next

        cur.next = nex

        prev = cur
        cur = nex
    return prev
