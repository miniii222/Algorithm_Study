# -*- coding: utf-8 -*-
3                                   
10 9                                 
2 0 1 0 0 0 1 0 0                       
1 2 8 7 1 3 1 1 2 5      
10 3       
2 2 2              
1 1 2 2 3 1 1 2 3 3              
3 3            
3 0 0             
1 2 3          
#%%input

NM = input().split()
NM = list(map(int, NM))
N = NM[0]; M = NM[1] #N 톨게이트를 통과한 차량정보, M 죄수들이 타고 있는 차량정보

prisoner = input().split(); prisoner = list(map(int, prisoner))
tollgate = input().split(); tollgate = list(map(int, tollgate))

#%%
def the_great_escape(prisoner, tollgate) :
    n = sum(prisoner) #M 죄수들이 타고 있는 차량개수
    
    for j in range(N-n+1) :
        prisoner2 = prisoner.copy()
        nn=0
        
        for car in tollgate[j:n+j] :
        
            if prisoner2[car-1] == 0 :
                break
            
            elif :
                prisoner2[car-1]-=1
                nn+=1                
                if nn==n :
                    return (j+1)
                    
    return 0

#%%output
T = int(input())

for tt in range(T) :
    NM = input().split()
    NM = list(map(int, NM))
    N = NM[0]; M = NM[1] #N 톨게이트를 통과한 차량정보, M 죄수들이 타고 있는 차량정보
    
    prisoner = input().split(); prisoner = list(map(int, prisoner))
    tollgate = input().split(); tollgate = list(map(int, tollgate))
    print("#{} {}".format(tt+1,the_great_escape(prisoner, tollgate)))
        
