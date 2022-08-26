# Homework 5
# Peter Bachman

class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next

    def __str__(self):
        return str(self.value)


class LinkedList:

    # Complexity class would be o(1) since it's running the same thing no
    # matter the size
    def __init__(self, value=None):
        self.head = Node(_value=value)
        self.tail = self.head
        self.length = 1

    def __checkValid(self, value, valueType):
        # Check if node value is an int or float
        if valueType == "nodeValue":
            if type(value) not in [float, int]:
                raise TypeError("Value must be an integer or float")

        # Check if node value is an integer
        if type == "position":
            if type(value) != int:
                raise TypeError("Value must be a integer")

    # Complexity class would be o(1) since it's running the same thing no
    # matter the size
    def length(self):
        return (self.length)

    # Complexity class would be o(1) since it's running the same thing no
    # matter the size
    def addNode(self, new_value):
        self.__checkValid(new_value, "nodeValue")
        self.tail.next = Node(new_value)
        self.tail = self.tail.next
        self.length += 1

    # Complexity class would be o(n) since it would increase with time based on
    # where the node is being placed
    # after_node indicates the position of the node to add it after,
    #   starting with 0
    def addNodeAfter(self, new_value, after_node):
        self.__checkValid(new_value, "nodeValue")
        self.__checkValid(after_node, "position")
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

    # Complexity class would be o(n) since it would increase with time based on
    # where the node is being placed
    # before_node indicates the position of the node to add it after,
    #   starting with 0
    def addNodeBefore(self, new_value, before_node):
        self.__checkValid(new_value, "nodeValue")
        self.__checkValid(before_node, "position")
        node = self.head
        i = 0
        while i < (before_node - 1):
            node = node.next
            i += 1
        oldNext = node.next
        node.next = Node(new_value, oldNext)
        self.length += 1

    # Complexity class would be o(n) since it would increase with time based on
    # where the node is being removed
    # node_to_remove indicates the position of the node to remove,
    #   starting with 0
    def removeNode(self, node_to_remove):
        self.__checkValid(node_to_remove, "position")
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

    # Complexity class would be o(n^2) since it would increase with time based
    # on going through the whole list to find values to remove, and
    # then removing them with the removeNode function.
    # where the node is being placed
    def removeNodesByValue(self, value):
        self.__checkValid(value, "nodeValue")
        node = self.head
        for i in range(self.length):
            try:
                if node.next.value == value:
                    self.removeNode(i + 1)
                node = node.next
            except AttributeError:
                break
            i += 1

    # Complexity class would be o(n) since it is dependent on the size of the
    # linked list
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

    # Complexity class would be o(n) since it is dependent on the size of the
    # linked list
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

    # Complexity class would be o(1) since it takes the same amount of time
    # independent of size
    def hasCycle(self):
        return self.tail.next == self.head
