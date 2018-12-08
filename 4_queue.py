class Queue :
    #데이터 추가
    def enqueue(self, data) :
        pass
    #데이터 제거
    def dequeue(self) :
        pass
    #is empty?
    def is_empty(self) :
        pass
    def is_full(self) :
        pass
    #display stack
    def display(self) :
        pass
    
#%%
class array_queue(Queue) :
    def __init__ (self, max_length) :
        self.items = []
        self.max_length = max_length
        self.size = 0
        
    def is_empty(self) :
        return self.size == 0
    
    def is_full(self) :
        return self.size == self.max_length
    
    def enqueue(self, data) :
        if self.is_full() :
            raise Exception("Queue is full")

        self.size +=1
        self.items.append(data)
        
    def dequeue(self) :
        if self.is_empty() :
            raise Exception("Queue is Empty")
        else :    
            dequeue_item = self.items.pop(0)
            self.size -=1
            return dequeue_item

    def display(self) :
        if self.is_empty() :
            raise Exception("Queue is empty!")
        else :
            return self.items
#%%
qu = array_queue(5)
qu.display()
qu.is_empty()
qu.enqueue(2)
qu.is_empty()
qu.enqueue(5)
qu.display()
qu.dequeue()
qu.display()
