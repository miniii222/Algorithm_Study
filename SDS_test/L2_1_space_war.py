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

NMB = input().split(' ')
NMB = list(map(int, NMB))
N = NMB[0]; M = NMB[1]; B = NMB[2] #N = 우주선 개수, M = 미사일 종류의 개수, B = 우주선의 방어막 세기

misile = [None]*M #misile정보
for i in range(M) :
    misile[i] = input().split(' ')
    misile[i] = list(map(int, misile[i]))
 
misile.sort()

misile_power = [None]*M; misile_num = [None]*M
for i in range(M) :
    misile_power[i] = misile[i][0]
    misile_num[i] = misile[i][1]
#%%

fit_index = [idx for idx in range(M) if misile_power[idx] == B]
over_index = [idx for idx in range(M) if misile_power[idx] > B]
answer = 0
over_B = []; below_B = []
below_B_power = misile_power; below_B_num = misile_num

if len(fit_index) > 0 : #misile의 파워가 방어막과 정확히 일치하는 경우가 있으면
    fit_sum = misile_num[fit_index[0]] #일치하는 미사일 개수
    
    if fit_sum*B >= N*B :
        answer = N*B #return
        
    else :
        N = N - fit_sum
        answer = fit_sum*B
       
    over_B_power = misile_power[fit_index[0]+1 :] #B보다 큰 경우
    over_B_num = misile_num[fit_index[0]+1 :]
    
    #2개이상인 미사일에 대하여 flatten하게 나열해서 적음.
    for i in range(len(over_B_power)) :
        over_B = over_B + [over_B_power[i]] * over_B_num[i]
        
    below_B_power = misile_power[:fit_index[0]] #B보다 작은 경우
    below_B_num = misile_num[:fit_index[0]]
          
elif len(over_index) > 0 :
    over_B_power = misile_power[over_index[0] :] #B보다 큰 경우
    over_B_num = misile_num[over_index[0] :]
    
    #2개이상인 미사일에 대하여 flatten하게 나열해서 적음.
    for i in range(len(over_B_power)) :
        over_B = over_B + [over_B_power[i]] * over_B_num[i]
           
    below_B_power = misile_power[:over_index[0]] #B보다 작은 경우
    below_B_num = misile_num[:over_index[0]]
    
#2개이상인 미사일에 대하여 flatten하게 나열해서 적음.
for i in range(len(below_B_power)) :
    below_B = below_B + [below_B_power[i]] * below_B_num[i]
below_i = [1]*len(below_B)
#%%
mysum = []

for i in range(len(below_B)-1) :
    for j in range(i+1, len(below_B)) :
        if below_B[i] + below_B[j] >=10 and below_i[i]>0 and below_i[j]>0 :
            below_i[i]-=1; below_i[j]-=1
            mysum+=[below_B[i] + below_B[j]]
           
#%%모든 케이스 큰거 작은거 자르지 않고
misile_flatten = [0]
for i in range(len(misile_power)) :
    misile_flatten = misile_flatten + [misile_power[i]] * misile_num[i]
misile_i = [sum(misile_num)]+[1]*(len(misile_flatten)-1)

mysum = []

for i in range(len(misile_flatten)-1) :
    for j in range(i+1, len(misile_flatten)) :
        if misile_flatten[i] + misile_flatten[j] >=10 and misile_i[i]>0 and misile_i[j]>0 :
            misile_i[i]-=1; misile_i[j]-=1
            mysum+=[misile_flatten[i] + misile_flatten[j]]
#%%      
mysum = mysum + over_B
mysum.sort()
answer = answer + sum(mysum[:N])
#%%new function
def space_war(misile, N, B) :
            
    fit_index = [index for index,value in enumerate(misile_power) if value == B]
    over_index = [index for index,value in enumerate(misile_power) if value > B]
    answer = 0
    
    if len(fit_index) > 0 : #misile의 파워가 방어막과 정확히 일치하는 경우
        fit_sum = misile_num[fit_index[0]] #일치하는 미사일 개수
        
        if fit_sum*B >= N*B :
            return N*B #return
            
        else :
            N = N - fit_sum
            answer = fit_sum*B
       
    over_B = []; below_B = []
    below_B_power = misile_power; below_B_num = misile_num
    
    if len(fit_index) > 0 and len(over_index) > 0 :    
        over_B_power = misile_power[fit_index[0]+1 :] #B보다 큰 경우
        over_B_num = misile_num[fit_index[0]+1 :]
        
        #2개이상인 미사일에 대하여 flatten하게 나열해서 적음.
        for i in range(len(over_B_power)) :
            over_B = over_B + [over_B_power[i]] * over_B_num[i]
            
        below_B_power = misile_power[:max(fit_index)] #B보다 작은 경우
        below_B_num = misile_num[:max(fit_index)]
            
    elif len(fit_index) > 0 :
        
        below_B_power = misile_power[:max(fit_index)] #B보다 작은 경우
        below_B_num = misile_num[:max(fit_index)]
        
        
    elif len(over_index) > 0 :
        over_B_power = misile_power[over_index[0] :] #B보다 큰 경우
        over_B_num = misile_num[over_index[0] :]
        
        #2개이상인 미사일에 대하여 flatten하게 나열해서 적음.
        for i in range(len(over_B_power)) :
            over_B = over_B + [over_B_power[i]] * over_B_num[i]
            
        
        below_B_power = misile_power[:over_index[0]] #B보다 작은 경우
        below_B_num = misile_num[:over_index[0]]
        
    #2개이상인 미사일에 대하여 flatten하게 나열해서 적음.
    for i in range(len(below_B_power)) :
        below_B = below_B + [below_B_power[i]] * below_B_num[i]
    below_i = [1]*len(below_B)

    mysum = []
    
    for i in range(len(below_B)-1) :
        for j in range(i+1, len(below_B)) :
            nowsum = below_B[i] + below_B[j]
            if nowsum >=10 and below_i[i]>0 and below_i[j]>0 :
                mysum+=[nowsum]
                below_i[i]-=1; below_i[j]-=1
                
    mysum = mysum + over_B
    if len(mysum)==0 :
        return -1
    
    mysum.sort()
    answer = answer + sum(mysum[:N])
    return answer

#%%input
T = int(input())

for tt in range(T) :
    NMB = input().split(' ')
    NMB = list(map(int, NMB))
    N = NMB[0]; M = NMB[1]; B = NMB[2] #N = 우주선 개수, M = 미사일 종류의 개수, B = 우주선의 방어막 세기

    misile = [None]*M #misile정보
    misile_power = [None]*M; misile_num = [None]*M
    
    for i in range(M) :
        misile[i] = input().split(' ')
        misile[i] = list(map(int, misile[i]))
        
    misile.sort()
    
    for i in range(M) :
        misile_power[i] = misile[i][0]
        misile_num[i] = misile[i][1]

    
    print("#{} {}".format(tt+1,space_war(misile_power,misile_num, N, B)))
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
