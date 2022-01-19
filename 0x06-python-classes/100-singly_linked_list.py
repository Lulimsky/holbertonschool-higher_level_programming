#!/usr/bin/python3


class Node:
    """node of a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """sets data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """sets the next_node of the Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
        """Defined singly-linked list"""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node to the linked list"""
        new = Node(value)
        
       if self.__head is None:
          self.__head = Node(value, None)
       elif self.__head.data => value:
            new = Node(value, self.__head)
	    self.__head = new

       else:
            ptr = self.__head
            while ptr.next_node is not None and ptr.next_node.data <= value:
                ptr = ptr.next_node

            tmp = ptr.next_node
            ptr.next_node = Node(value, tmp)

    def __str__(self):
        """"printable list"""
        ptr = self.__head
        prilis = ""
        while ptr is not None:
            prilis = prilis + str(ptr.data) + '\n'
            ptr = ptr.next_node
        return prilis[:-1]
