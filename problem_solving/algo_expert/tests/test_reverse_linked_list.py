def reverse_linked_list(head):
    cur = head
    prev = None

    while cur:
        nex = cur.next

        cur.next = prev

        prev = cur
        cur = nex

    return prev


def reverseLinkedListRecursive(head, prev=None):
    if head:
        nex = head.next
        head.next = prev
        return reverseLinkedListRecursive(prev=head, head=nex)
    return prev


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def test_positve_case():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    """
    1->2->3->4>-5->None
    5->4->3->2->1->None
    
    None <- 1 <- 2 -> 3 -> 4 -> 5 -> None
            ^    ^    ^
            |    |    |
           prev  cur  nex
        
    """

    head = reverse_linked_list(one)

    while head:
        print(head.value, end="->")
        head = head.next
    print("None")


if __name__ == '__main__':
    test_positve_case()
    # test_positve_case_in_recursive_soln()
