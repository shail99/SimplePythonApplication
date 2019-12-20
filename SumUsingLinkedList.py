
acc_sum = ""
carry = 0
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class LinkedList(object):
    def __init__(self, root):
        self.root = root


def add(l1, l2):
    if l1 is None:
        return 0

    add(l1.next, l2.next)
    global acc_sum
    global carry

    acc_sum = str((l1.value + l2.value + carry) % 10) + acc_sum
    carry = int((l1.value + l2.value) / 10)


if __name__ == '__main__':
    a1 = Node(3)
    a2 = Node(6)
    a3 = Node(7)
    a1.set_next(a2)
    a2.set_next(a3)

    b1 = Node(9)
    b2 = Node(8)
    b3 = Node(2)
    b1.set_next(b2)
    b2.set_next(b3)

    a = LinkedList(a1)
    b = LinkedList(b1)
    add(a.root, b.root)
    print(str(carry) + acc_sum)