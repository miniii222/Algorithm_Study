#%%
class Stack :
    #데이터 추가
    def push(self, data) :
        pass
    #데이터 제거
    def pop(self) :
        pass
    #is empty?
    def is_empty(self) :
        pass
    #is full?
    def is_full(self) :
        pass
    #display stack
    def display(self) :
        pass
    
#%%
#array_stack
class array_stack(Stack) :
    def __init__(self, max_length) :
        self.items = []
        self.top = 0
        self.max_length = max_length
        
    def is_empty(self) :
        return self.top==0
    
    def is_full(self) :
        return self.top==self.max_length
    
    def push(self, data) :
        if self.is_full():
            raise Exception("Stack is full!")
            
        self.top+=1
        self.items.append(data)
        
    def pop(self) :
        if self.is_empty() :
            raise Exception("Stack is empty!")
            
        data = self.items[-1]
        del self.items[-1]
        self.top-=1
        
        return data
    
    def display(self) :
        if self.is_empty() :
            raise Exception("Stack is empty!")
        else :
            return self.items

#%%    
stk = array_stack(5)
stk.is_empty()
stk.display()
stk.push(2)
stk.push(5)
stk.display()
stk.pop()
stk.display()
stk.push(3)
stk.display()

#%%
class linked_stack(Stack) :
    def __init__(self) :
        self.items = []
        self.top = 0
        self.max_length = 20
        
    def is_empty(self) :
        return self.top==0
    
    def is_full(self) :
        return self.top==self.max_length
    
    def push(self, data) :
        if self.is_full():
            raise Exception("Stack is full!")
            
        self.top+=1
        self.items.append(data)
        
    def pop(self) :
        if self.is_empty() :
            raise Exception("Stack is empty!")
            
        data = self.items[-1]
        del self.items[-1]
        self.top-=1
        
        return data
    
    def display(self) :
        if self.is_empty() :
            raise Exception("Stack is empty!")
        else :
            return self.items
