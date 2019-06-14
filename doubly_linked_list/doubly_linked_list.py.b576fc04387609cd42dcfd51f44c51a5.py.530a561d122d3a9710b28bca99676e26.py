from math import inf

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        current_head = self.head
        new_head = ListNode(value)

        if not current_head:
            self.head = new_head
        else:
            current_head.insert_before(value)
            self.head = current_head.prev
            self.length += 1

    def remove_from_head(self):

        if not self.head:
            return None
        removed_head = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.head.delete()
            self.head = self.head.next
            self.tail = self.tail.next
            self.length += 1

        return removed_head

    def add_to_tail(self, value):
        if self.tail is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

        self.length += 1

    def remove_from_tail(self):
        if not self.tail:
            return None
        removed_tail = self.tail.value
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail.delete()
            self.tail = self.tail.prev
        self.length -= 1
        return removed_tail

    def move_to_front(self, node):
        if self.head is not node:
            if node.next and node.prev:
                node.delete()
            current_head = self.head
            self.head = node
            node.next = current_head
            current_head.prev = node

    def move_to_end(self, node):
        if node != self.tail:
            self.tail.insert_after(node.value)
            self.tail = self.tail.next
        if node == self.head:
            self.head = node.next

    def delete(self, node):
        if node == None:
            return
        if len(self) < 2:
            node.delete()
            self.head = None
            self.tail = None
            self.length -= 1
        if len(self) == 2:
            node.delete()
            self.length -= 1
            if node == self.head:
                self.head = self.tail
                self.tail.prev = None
            else:
                self.tail = self.head
                self.head.next = None
            return

        if node == self.head:
            node_next = self.head.next
            self.head = node_next
        elif node == self.tail:
            node_prev = self.tail.prev
            self.tail = node_prev
        node.delete()
        self.length -= 1


    def get_max(self):
        cur = self.head
        max = -inf
        while cur != None:
            if cur.value > max:
                max = cur.value
            cur = cur.next
        return max
