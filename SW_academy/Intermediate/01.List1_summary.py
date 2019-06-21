# -*- coding: utf-8 -*-

# Exhaustive Search - 모든 경우를 탐색. 속도는 느리지만 틀리지 않음

## 1,2,3을 포함하는 모든 순열을 생성하는 코드
for i1 in range(1,4) :
    for i2 in range(1,4) :
        if i2 != i1 :
            for i3 in range(1,4) :
                if i3 != i1 and i3 != i2 :
                    print(i1, i2, i3)


# Greedy Algorithm - 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식. 전체 최적이라는 보장 없음
# 해 선택 -> 실행 가능성 검사 -> 해 검사
                    
## Baby-gin 문제
num = 456789
c = [0] * 12

for i in range(6) :
    c[num % 10] += 1
    num //= 10
    
i = 0
tri = run = 0

while i < 10 :
    if c[i] >= 3 : #triplet 확인
        c[i] -=3
        tri +=1
        continue;
        
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 :
        c[i] -=1
        c[i+1] -=1
        c[i+2] -=1
        
        run +=1
        continue
    i +=1
    
if run + tri ==2 :
    print('Baby Gin')

# 답을 찾지 못하는 경우도 있음
    
# Bubble Sort -> 시간 복잡도 O(n^2)
# Counting Sort -> 식나 복잡도 O(n + k) n : 리스트의 개수 / k : 정수의 최댓값 
## 시간 복잡도가 1차이지만, n이 너무 커지면 메모리 에러 가능성이 있음

def CountingSort(A, B, k) :
    #A(n) : 입력 리스트 사용된 숫자(1 ~ k)
    #B(n) : 정렬된 리스트
    #C(k) : 카운트 리스트
    
    C = [0] * k
    
    for i in range(len(B)) :
        C[A[i]] += 1 #각 숫자들이 몇 개인지 센다
        
    for i in range(1, len(C)) :
        C[i] += C[i-1] #누적합을 구함으로써 각 숫자들의 정렬 후 마지막 위치를 저장
        
    for i in range(len(B) -1, -1, -1) :
        B[C[A[i]]-1] = A[i]
        C[A[i]]-=1
    
