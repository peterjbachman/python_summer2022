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
        if after_node >= self.length:
            raise AttributeError("Position is out of bounds")
        if after_node == self.length - 1:
            self.addNode(new_value)
        else:
            while i < after_node:
                node = node.next
                i += 1
            oldNext = node.next
            node.next = Node(new_value, oldNext)
        self.length += 1

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
        self.length += 1

    # Complexity class would be o()
    # node_to_remove indicates the position of the node to remove,
    #   starting with 0
    def removeNode(self, node_to_remove):
        node = self.head
        i = 0
        if node_to_remove == 0:
            self.head = node.next
        else:

            while i < (node_to_remove - 1):
                node = node.next
                i += 1
            beforeNode = node
            try:
                middleNode = beforeNode.next
                afterNode = middleNode.next
                beforeNode.next = afterNode
            except AttributeError:
                beforeNode.next = None
        self.length -= 1

    # Complexity class would be o()
    def removeNodesByValue(self, value):
        node = self.head
        for i in range(self.length):
            try:
                if node.next.value == value:
                    self.removeNode(i + 1)
                node = node.next
            except AttributeError:
                break
            i += 1

    def reverse(self):
        prevNode = None
        currentNode = self.head
        tailNode = self.head
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.head = prevNode
        self.tail = tailNode

    # Complexity class would be o()
    def __str__(self):
        node = self.head
        nonTail = True
        linkedNodes = ""

        while nonTail:
            linkedNodes += str(node)
            if node.next is None or node.next == self.head:
                nonTail = False
                break
            else:
                linkedNodes += " -> "
                node = node.next
        return linkedNodes

    # Complexity class would be o()
    def hasCycle(self):
        return self.tail.next == self.head
