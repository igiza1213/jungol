class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            return self.stack.pop()
        else:
            return "empty"

    def isEmpty(self):
        if self.size():
            return True
        else:
            return False

    def size(self):
        return len(self.stack)

    def peek(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            return self.isEmpty()

    def __str__(self):
        return str(self.stack)

stack = Stack()

N = int(input())

for _ in range(N):
    flag, *value = input().split()

    if flag == "i":
        stack.push(int(value[0]))
    elif flag == "o":
        print(stack.pop())
    elif flag == "c":
        print(stack.size())

