class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.max_size = 5

    def push(self, data):
        if not self.is_full():
            self.stack.append(data)
        else:
            print("stack이 가득 찼습니다.")

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            print("stack이 비었습니다.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("stack이 비었습니다.")

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def is_full(self):
        if len(self.stack) == self.max_size:
            return True
        else:
            return False
    def display(self):
        return self.stack

if __name__=="__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    print(stack.display())


