class Node(object):
    def __init__(self):
        self.value = 0
        self.next = None

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next


class LinkedList(object):
    def __init__(self):
        self.root = None

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def print(self):
        temp = self.root
        while temp:
            print(temp.get_value())
            temp = temp.get_next()

    def reverse(self):
        prev = None
        current = self.root
        while current:
            temp = current.get_next()
            current.set_next(prev)
            prev = current
            current = temp
        self.root = prev

    def reverse_rec(self, current):
        if current is None or current.get_next() is None:
            self.root = current
            return
        self.reverse_rec(current.get_next())
        current.get_next().set_next(current)
        current.set_next(None)


if __name__ == '__main__':
    linked_list = LinkedList()
    n1 = Node()
    n2 = Node()
    n3 = Node()
    n4 = Node()
    n1.set_value(1)
    n2.set_value(2)
    n3.set_value(3)
    n4.set_value(4)
    n1.set_next(n2)
    n2.set_next(n3)
    n3.set_next(n4)
    linked_list.set_root(n1)
    linked_list.print()
    linked_list.reverse_rec(linked_list.get_root())
    print("Reversed")
    linked_list.print()
