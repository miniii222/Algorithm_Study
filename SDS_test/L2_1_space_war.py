# -*- coding: utf-8 -*-

#시간초과....
2

4 7 10
8 2
7 1
6 2
5 2
4 1
12 2
10 1


2 3 10
6 1
4 1
12 2

2 4 10
3 3
5 1
1 5
10 1

#answer = 42
#%%input
#T = int(input())
#i = 1
NMB = input().split(' ')
NMB = list(map(int, NMB))
N = NMB[0]; M = NMB[1]; B = NMB[2] #N = 우주선 개수, M = 미사일 종류의 개수, B = 우주선의 방어막 세기

misile = [None]*M #misile정보

for i in range(M) :
    misile[i] = input().split(' ')
    misile[i] = list(map(int, misile[i]))
 
misile.sort()   
#%%
fit_index = [index for index,value in enumerate(misile) if value[0] == B]
answer = 0
if len(fit_index)>0 :
    B_misile = misile.pop(fit_index[0]) #B와 정확히 일치하는 미사일은 제거

    if (N - B_misile[1]) <= 0 :
        #end
        answer = N*B
        
    else :
        N = N - B_misile[1]
        answer = B
#%%
misile_num = [ misile[i][1] for i in range(len(misile)) ]
misile_power = []

#2개이상인 미사일에 대하여 flatten하게 나열해서 적음.
for i in range(len(misile)) :
    misile_power = misile_power + [misile[i][0]] * misile_num[i]

over_B = [index for index,value in enumerate(misile_power) if value > B]
below_B = misile_power[:over_B[0]] #power가 B보다 작은 모음
#%%
mysum = []
for j in range(len(below_B)-2) :
    for i in range(len(below_B)-1) :
        now_sum = below_B[j] + below_B[i+1]
        if now_sum == B :
            N-=1
            answer += B
            if N <= 0 :
                
                break
                break
        elif now_sum > B :        
            mysum = mysum + [now_sum]
#%%      
mysum = mysum + misile_power[over_B[0]:]
mysum.sort()

answer = answer + sum(mysum[:N])
#%%
def space_war(misile, N, M, B) :
    fit_index = [index for index,value in enumerate(misile) if value[0] == B] #B와 정확히 일치하는 미사일 찾기
    
    answer = 0
    if len(fit_index)>0 :
        B_misile = misile.pop(fit_index[0]) #B와 정확히 일치하는 미사일은 제거
    
        if (N - B_misile[1]) <= 0 :
            #end
            answer = N*B
            return answer
            
        else :
            N = N - B_misile[1]
            answer = B *len(fit_index)

    misile_num = [ misile[i][1] for i in range(len(misile)) ] #미사일 개수 모음
    misile_power = []
    
    #2개이상인 미사일에 대하여 파워만 flatten하게 나열해서 적음.
    for i in range(len(misile)) :
        misile_power = misile_power + [misile[i][0]] * misile_num[i]
    
    over_B = [index for index,value in enumerate(misile_power) if value > B]
    
    if len(over_B) == 0 :
        below_B = misile_power
    else :
        below_B = misile_power[:over_B[0]] #power가 B보다 작은 모음
    
    mysum = []
    if len(below_B) <= 2 :
        now_sum = sum(below_B)
        if now_sum == B :
            N-=1
            answer+=B
            if N==0 :
                return answer
        elif now_sum > B :
            mysum = mysum + [now_sum]
            
    else :        
        for j in range(len(below_B)-2) :
            for i in range(len(below_B)-1) :
                now_sum = below_B[j] + below_B[i+1]
                if now_sum == B :
                    N-=1
                    answer += B
                    #if N == 0 :
                        #return answer
                        
                elif now_sum > B :        
                    mysum = mysum + [now_sum]
    
    if len(over_B) > 0 :
        mysum = mysum + misile_power[over_B[0]:]

    mysum.sort()
    
    if len(mysum) ==0 :
        return -1
    
    answer = answer + sum(mysum[:N])
    return answer

#%%
T = int(input())

for tt in range(T) :
    NMB = input().split(' ')
    NMB = list(map(int, NMB))
    N = NMB[0]; M = NMB[1]; B = NMB[2] #N = 우주선 개수, M = 미사일 종류의 개수, B = 우주선의 방어막 세기
    
    misile = [None]*M #misile정보
    
    for i in range(M) :
        misile[i] = input().split(' ')
        misile[i] = list(map(int, misile[i]))
     
    misile.sort()
    print("#{} {}".format(tt+1,space_war(misile, N,M,B)))
