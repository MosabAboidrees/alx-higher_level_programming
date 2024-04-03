#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Defines a node of a singly linked list.
    Attributes:
        data (int): The data held by the node.
        next_node (Node): The next node in the list.
    """
    
    def __init__(self, data, next_node=None):
        """Initialize a Node with data and
        optionally a reference to the next node.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node in the list. Defaults to None.
        """
        self.data = data  # Set the node's data
        self.next_node = next_node  # Set the next node; defaults to None

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the node's data, ensuring it is an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node, ensuring it is either None or a Node object."""
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list with methods for
    sorted insertion and string representation.
    
    This class provides the functionality to maintain 
    a sorted singly linked list. Nodes can be inserted in an order, 
    and the list can be represented as a string.
    """
    
    def __init__(self):
        """Initialize the singly linked list with no head node."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the list in sorted (ascending) order.
        
        This method creates a new Node with the provided value 
        and inserts it into the list while maintaining sorted order.
        
        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)  # Create a new Node with the given value
        if self.__head is None or self.__head.data >= value:
            # If list is empty or new node should be first,
            # insert it at the beginning
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Find the insertion point
            current = self.__head
            while current.next_node is not None and
            current.next_node.data < value:
                current = current.next_node
            # Insert new node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the list,
        one node's data per line."""
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))  # Add the node's data to the list
            current = current.next_node
        return "\n".join(nodes)  # Join all node data strings
