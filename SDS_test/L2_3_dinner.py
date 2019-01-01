# -*- coding: utf-8 -*-
8
7 3  
12 1  
2 9  
11 7  
7 2  
4 3  
9 4  
5 5    
#%%input
N = int(input()) #점의 개수

xy = [None]*N
for i in range(N) :
    xy[i] = input().split(' ')
    xy[i] = list(map(int, xy[i]))
    
#%%function
def dinner(xy) :
    
    xy2 = [(i+1,a) for i,a in enumerate(xy)]
    xy.sort()
    
    #xy_idx = [i[0] for i in xy]
    
    res = [idx for idx, value in xy2 if value == xy[0]]
    
    for i in range(1,N) :
        aa = 0
        for xyxy in xy[:i] :
            if xyxy[1]<=xy[i][1] :
                break
            aa+=1
        if aa == i :
            res+=[idx for idx, value in xy2 if value == xy[i]]
            #res+=[xy[i]]
            
    
    return res
    #return [idx+1 for idx in xy_idx if idx not in fail]
[i+1 for i in range(8) if xy2[i][1]==xy[0]]
#%%output
T = int(input())

for tt in range(T+1) :
    N = int(input()) #점의 개수

    xy = [None]*N
    for i in range(N) :
        xy[i] = input().split(' ')
        xy[i] = list(map(int, xy[i]))
    
    answer = " ".join(str(x) for x in dinner(xy))
    print("#{} {}".format(tt+1, answer))
#%%
answer = dinner(xy)
print("#{}".format(2), end = " ")
for x in dinner(xy) :
    print(x, end = " ")
          
