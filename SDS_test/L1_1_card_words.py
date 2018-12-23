# -*- coding: utf-8 -*-
5  
3  
E O T  
7  
J S M F G S Z   
7  
I H G Y Q D D   
7  
S Z B D A Q T   
10  
D Q Q V L W K G G I  
#%%
N = int(input())
words = input().split(" ")

answer = words[0]

for i in range(N-1) :
    if answer[0]<=words[i+1] :
        answer = words[i+1]+answer
    else :
        answer = answer+words[i+1]
        
#%%output
T = int(input())

for tt in range(T) :
    N = int(input())
    words = input().split(" ")
    
    answer = words[0]
    
    for i in range(N-1) :
        if answer[0]<=words[i+1] :
            answer = words[i+1]+answer
        else :
            answer = answer+words[i+1]
    
    print("#{} {}".format(tt+1,answer))