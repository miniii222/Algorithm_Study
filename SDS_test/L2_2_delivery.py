# -*- coding: utf-8 -*-
2
7 11 2 7
1 5

1 2
4 5
6 1
3 4
5 3
3 6
7 6
6 2
7 2
3 1
5 7

10 13 3 9
4 5 2

9 2
8 3
1 10
8 4
8 6
4 6
6 3
7 5
5 9
9 10
8 5
8 9
1 4
#%%input
T = int(input())
NMKS = input().split(' ')
NMKS = list(map(int, NMKS))
N = NMKS[0]; M = NMKS[1]; K = NMKS[2]; S = NMKS[3] #N = 마을 수, M = 도로 수, K = 배달해야 하는 마을 개수, S = 시작 마을
N,M,K,S = raw_input().split()

#배달할 마을 번호
delivery = input().split(' ')
delivery = list(map(int, delivery))

#road_matrix = [[0] * N]*N #연결 도로 정보 이렇게 하면 생성된 하나의 리스트 한개가 여러개가 생기는 효과. 하나만 바꿔도 바뀜 ㄷㄷ

road_matrix = [[0 for x in range(N)] for y in range(N)]

for i in range(M) :
    road=input().split(' ')
    road = list(map(int, road))
    
    road_matrix[road[0]-1][road[1]-1] = 1 #연결된 경우만 1로

road_matrix_t = list(map(list, zip(*road_matrix)))

road_sum = []
for road_row in range(N) :
    road_sum.append([first + second for first, second in zip(road_matrix[road_row], road_matrix_t[road_row])])

#%%symmetric matrix multiplication
def matrixmulti (A):
    C = [[0 for x in range(N)] for y in range(N)]
    
    for j in range(N) :
        for i in range(N) :
            C[j][i] = sum( [a*b for a,b in zip(A[j], A[i]) ])
    
    return C
#%%
def find_route(start, end) :
    n=0
    if road_sum[start-1][end-1]>0 :
        n+=1
        
    else :
        n=2
        mymat = matrixmulti(road_sum)
        while mymat[start-1][end-1] <= 0 :
            mymat = matrixmulti(mymat)
            n+=1
            
    return n
#%%
answer = find_route(S,delivery[0])
for i in range(K-1):
    answer+=find_route(delivery[i],delivery[i+1])

answer += find_route(delivery[K-1],S)

#%%generate village
village = dict()

for j in range(N) :
    idx = [index+1 for index,value in enumerate(road_sum[j]) if value == 1]
    village[j+1] = idx
#%%

