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

    xy = [(i+1,a) for i,a in enumerate(xy)]
    xy.sort(key = lambda x : x[1])
    
    fail = []
    for i in range(1,N) :
        for xyxy in xy2[:i] :
            if xyxy[1]<=xy2[i][1] :
                fail.append(xy2[i]) #후보에서 탈락한 레스토랑 목록
                break
    return [i for i, rest in xy if rest not in fail]

#%%output
T = int(input())

for tt in range(T) :
    N = int(input()) #점의 개수

    xy = [None]*N
    for i in range(N) :
        xy[i] = input().split(' ')
        xy[i] = list(map(int, xy[i]))
        
    print("#{} ".format(tt+1), end = "")
    dd = dinner(xy)
    for answer in dd :
        print(answer, end = " ")
    print("")
          
