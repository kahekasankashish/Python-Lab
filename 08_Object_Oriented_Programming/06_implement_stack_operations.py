# Q6. Define a Stack class with member functions to perform basic stack operations and demonstrate them.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack is empty - underflow condition.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Elements in the stack are:")
        for item in reversed(self.items):
            print(item)

stack = Stack()
stack.push(1)
stack.push(3)
stack.push(6)
stack.display()
removed = stack.pop()
if removed is not None:
    print(removed, "is removed.")
stack.display()
