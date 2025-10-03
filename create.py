class Stack:
    def __init__(self):
        self.stack = []   # using a list to store stack elements

    
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        removed_item = self.stack.pop()
        print(f"{removed_item} popped from stack")
        return removed_item

    
    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        return self.stack[-1]

    
    def is_empty(self):
        return len(self.stack) == 0

    
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements (top -> bottom):", " -> ".join(map(str, reversed(self.stack))))


# 🧪 Example Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Top element is:", s.peek())

s.pop()
s.display()

s.pop()
s.pop()
s.pop()  # extra pop to show empty handling
