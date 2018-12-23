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
    
    xy2 = xy.copy()
    xy2.sort()
    
    xy = [(i,a) for i,a in enumerate(xy)]
    xy.sort(key = lambda x : x[1])
    
    xy_idx = [i[0] for i in xy]
    
    fail = []

    for i in range(1,N) :
        for xyxy in xy2[:i] :
            if xyxy[1]<=xy2[i][1] :
                fail+= [ xy_idx[i] ]
                break
        
    return [idx+1 for idx in xy_idx if idx not in fail]

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

          
