class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.no_of_nodes = 0

    # O(1)
    def insert_start(self, data):
        self.no_of_nodes += 1
        new_node = Node(data)

        if self.head:
            new_node.next_node = self.head

        self.head = new_node

    # O(N)
    def insert_end(self, data):
        self.no_of_nodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            actual_node = self.head
            while actual_node.next_node:
                actual_node = actual_node.next_node
            actual_node.next_node = new_node

    # O(N)
    def remove(self, data):
        if self.head:
            actual_node = self.head
            previous_node = None

            while actual_node and actual_node.data != data:
                previous_node = actual_node
                actual_node = actual_node.next_node

            if actual_node:  # present
                self.no_of_nodes -= 1

                if not previous_node:
                    self.head = actual_node.next_node
                else:
                    previous_node.next_node = actual_node.next_node

    # O(1)
    def size(self):
        return self.no_of_nodes

    # O(N)
    def print(self):
        actual_node = self.head
        while actual_node:
            print(actual_node.data, end=' ')
            actual_node = actual_node.next_node

        print()  # line break
