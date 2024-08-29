class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("큐에 데이터가 없습니다.")
        else:
            self.queue.pop(0)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    
    def display(self):
        print(self.queue)

    
if __name__=="__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    # [2,3]
    queue.display()
    