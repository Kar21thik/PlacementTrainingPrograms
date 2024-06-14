class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # Initialize the stack with an empty head

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point new node's next to the current head
        self.head = new_node  # Update head to the new node
        print(f"Pushed {data} to stack")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.head  # Store the current head
        self.head = self.head.next  # Update head to the next node
        return popped_node.data  # Return the popped node's data

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.head.data  # Return the top element's data without removing it

    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Example Usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()  # Output: 30 -> 20 -> 10 -> None
    print(f"Popped: {stack.pop()}")  # Output: Popped: 30
    print(f"Top element: {stack.peek()}")  # Output: Top element: 20
    stack.print_stack()  # Output: 20 -> 10 -> None
    print(f"Stack is empty: {stack.is_empty()}")  # Output: Stack is empty: False
    stack.pop()
    stack.pop()
    print(f"Stack is empty: {stack.is_empty()}")  # Output: Stack is empty: True
    stack.print_stack()  # Output: None
