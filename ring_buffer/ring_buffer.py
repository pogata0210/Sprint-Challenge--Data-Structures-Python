class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity
        
        

    def append(self, item):
        if self.current == len(self.storage):
            self.current = 0
        self.storage[self.current] = item
        #detatch element to current index in item        
        self.current += 1
        #increment to the beginning
        
        

    def get(self):
        temp = []
        for n in range(0, len(self.storage)):
            if self.storage[n] != None:
                temp.append(self.storage[n])
        return temp