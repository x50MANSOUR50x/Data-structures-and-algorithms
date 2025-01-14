class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def print_list(self) -> None:
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next
    
    def append(self, value) -> None:
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.next = self.head
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value) -> None:
            new_node = Node(value=value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                self.head.next = self.tail
                self.tail.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
            self.length += 1
    
    def pop(self) -> Node | None:
        if self.length  == 0:  # Handle empty list
            return None
        temp = self.head
        if self.length  == 1:  # Handle single node
            self.head = None
            self.tail = None
            self.length  -= 1
            return temp

        # Traverse to the second-to-last node
        for _ in range(self.length  - 2):
            temp = temp.next

        last_node = temp.next  # Last node to be removed
        self.tail = temp       # Update tail to second-to-last node
        self.tail.next = self.head  # Maintain circular link
        self.length  -= 1       # Decrement length

        return last_node

    def pop_first(self) -> Node|None:
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next 
            temp.next = None
            self.tail.next = self.head
        self.length -= 1
        return temp
    
my_list = CircularLinkedList()
my_list.print_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.print_list()
        