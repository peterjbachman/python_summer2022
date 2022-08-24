# Homework 5
# Peter Bachman

class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next

    def __str__(self):
        return str(self.value)


class LinkedList:

    # Complexity class would be o()
    def __init__(self, value=None):
        self.head = Node(_value=value)
        self.tail = self.head
        self.length = 1

    # Complexity class would be o()
    def length(self):
        return (self.length)

    # Complexity class would be o()
    def addNode(self, new_value):
        self.tail.next = Node(new_value)
        self.tail = self.tail.next
        self.length += 1

    # Complexity class would be o()
    # after_node indicates the position of the node to add it after,
    #   starting with 0
    def addNodeAfter(self, new_value, after_node):
        node = self.head
        i = 0
        while i < after_node:
            node = node.next
            i += 1
        oldNext = node.next
        node.next = Node(new_value, oldNext)

    # Complexity class would be o()
    # before_node indicates the position of the node to add it after,
    #   starting with 0
    def addNodeBefore(self, new_value, before_node):
        node = self.head
        i = 0
        while i < (before_node - 1):
            node = node.next
            i += 1
        oldNext = node.next
        node.next = Node(new_value, oldNext)

    # Complexity class would be o()
    def __str__(self):
        node = self.head
        nonTail = True
        linkedNodes = ""
        while nonTail:
            linkedNodes += str(node)
            node = node.next
            if node is None:
                nonTail = False
                break
            else:
                linkedNodes += " -> "
        return linkedNodes

    # Complexity class would be o()
    def hasCycle(self):
        return self.tail.next == self.head


test = LinkedList(1)
test.addNode(2)
test.addNode(3)
print(test)

test.addNodeAfter(5, 1)
print(test)

test.addNodeBefore(7, 1)
print(test)
