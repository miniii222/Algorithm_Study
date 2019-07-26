# -*- coding: utf-8 -*-
'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''
#%%
T = int(input())

for tt in range(T) :
    n = int(input())

    NN = []
    
    for i in range(n) :
        a = list(map(int, input().split()))
        NN.append(a)

    answer = []
    for sign in [1,-1] :
            queue = [[sign]]
                    
            while queue:
                path = queue.pop(0)
                
                if len(path)==(n -1 + n - 1) : # path length : (n + n - 1)
                    if sum(path) == 0 :
                        i, j = 0,0
                        mysum = NN[i][j]
                                            
                        for pp in path :
                            #오른쪽
                            if pp == 1 :
                               j += 1
                               mysum += NN[i][j]
                            
                            elif pp == -1 :
                                i += 1
                                mysum += NN[i][j]
                            
                        answer.append(mysum)
                               
                    
                else:
                    for m in [1,-1]:
                        queue.append(path + [m])

    print('#{} {}'.format(tt+1,min(answer)))