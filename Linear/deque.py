class Deque:
    def __init__(self) -> None:
        self.deque = []

    def add_front(self, data):
        self.deque.insert(0, data)

    def add_rear(self, data):
        self.deque.append(data)

    def remove_front(self):
        if self.is_empty():
            pass
        else: 
            self.deque.pop(0)
        
    def remove_rear(self):
        if self.is_empty():
            pass
        else: 
            self.deque.pop()     
    
    def is_empty(self):
        return len(self.deque)==0

    def display(self):
        print(self.deque)

if __name__=="__main__":
    deque = Deque()
    deque.add_rear(1)
    deque.add_rear(2)
    deque.add_front(0)
    # [0, 1, 2]
    deque.display()