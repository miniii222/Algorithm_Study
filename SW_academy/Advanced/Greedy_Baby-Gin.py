# -*- coding: utf-8 -*-
'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
1 3 1 1 1 3 2 0 2 4 7 8
'''
#%%
'''
0 0 0 0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2 2 2 2
'''
#%%
T = int(input())
for tt in range(T) :
    N = list(map(int, input().split()))
    A = 0; B =0
    A_num = {N[0]:1}; B_num = {N[1] : 1}
    
    for i, n in enumerate(N[2:]) :       
        i+=2
        #user A
        if i%2 ==0 :
            ##triplet
            if n in A_num :
                A_num[n]+=1
                if A_num[n] == 3 :
                    A = i//2
            else :
                A_num[n]=1
        
            ##run
            A_list = list(A_num.keys())
            if (n-1 in A_list) and (n+1 in A_list) :
                A = i//2
            if (n-1 in A_list) and (n-2 in A_list) :
                A = i//2
            if (n+1 in A_list) and (n+2 in A_list) :
                A = i//2
        #user B    
        else :
            ##triplet
            if n in B_num :
                B_num[n]+=1
                if B_num[n] == 3 :
                    B = i//2
            else :
                B_num[n]=1
                
            ##run
            B_list = list(B_num.keys())
            if (n-1 in B_list) and (n+1 in B_list) :
                B = i//2
            if (n-1 in B_list) and (n-2 in B_list) :
                B = i//2
            if (n+1 in B_list) and (n+2 in B_list) :
                B = i//2

    
        if (i == len(N)-1) and (A == B) :
            print('#{} {}'.format(tt+1, 0))
            break
        elif A > B :
            print('#{} {}'.format(tt+1, 1))
            break
        elif A < B :
            print('#{} {}'.format(tt+1, 2))
            break      
#%%



