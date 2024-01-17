#!/usr/bin/python3

class Node:
    """Node class for a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initializes a new Node instance.

        Args:
            data: The data value for the node.
            next_node (Node, optional): The next node in the linked list.
        """
        self.data = data  # Using the setter to perform validation
        self.next_node = next_node  # Using the setter to perform validation

    @property
    def data(self):
        """Getter method to retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data.

        Args:
            value: The new value for the data attribute.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next node.

        Args:
            value: The new value for the next_node attribute.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class."""
    def __init__(self):
        """Initializes a new SinglyLinkedList instance with an empty list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list

        Args:
            value: The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not \
                    None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the SinglyLinkedList."""
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
