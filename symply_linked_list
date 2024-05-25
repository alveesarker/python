class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data of the node
        self.next = None  # Initialize the next pointer to None


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None

    def add_begin(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Point the new node's next to the current head
        self.head = new_node  # Update the head to the new node

    def add_end(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:
            self.head = new_node  # If the list is empty, set the head to the new node
        else:
            n = self.head
            while n.next is not None:  # Traverse to the end of the list
                n = n.next
            n.next = new_node  # Link the last node to the new node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:  # Find the node after which the new node should be added
                break
            n = n.next
        if n is None:
            print("Node is not found.")
        else:
            new_node = Node(data)  # Create a new node
            new_node.next = n.next  # Link the new node's next to the current node's next
            n.next = new_node  # Link the current node to the new node

    def add_before(self, data, x):
        if self.head is None:
            print("Node is not found.")
            return
        new_node = Node(data)  # Create a new node
        if self.head.data == x:  # If the head node is the target node
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:  # Find the node before which the new node should be added
                break
            n = n.next
        if n.next is None:
            print("Node is not found.")
        else:
            new_node.next = n.next  # Link the new node's next to the target node
            n.next = new_node  # Link the current node to the new node

    def delete_begin(self):
        if self.head is None:
            print("The Linked list is empty.")
        else:
            self.head = self.head.next  # Update the head to the next node

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head = None  # If there's only one node, set head to None
        else:
            n = self.head
            while n.next.next is not None:  # Traverse to the second last node
                n = n.next
            n.next = None  # Remove the last node

    def delete_specific(self, x):
        if self.head is None:
            print("Linked list is empty.")
        elif x == self.head.data:
            self.head = self.head.next  # If the head is the target node, update the head
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:  # Find the node to be deleted
                    break
                n = n.next
            if n.next is None:
                print('Node is not found.')
            else:
                n.next = n.next.next  # Remove the target node

    def traverse(self):
        if self.head is None:
            print('List is empty.')
        else:
            n = self.head
            while n is not None:
                print(n.data, end="-->")  # Print the data of each node
                n = n.next
            print('end')


# Example usage
linked_list = LinkedList()

# Adding nodes to the linked list
linked_list.add_begin(78)
linked_list.add_begin(98)
linked_list.add_begin(34)
linked_list.add_end(56)
linked_list.add_after(30, 56)
linked_list.add_before(57, 34)
linked_list.add_before(99, 78)

# Deleting nodes from the linked list
linked_list.delete_begin()
linked_list.delete_end()
linked_list.delete_specific(66)

# Traverse the linked list to display the elements
linked_list.traverse()
