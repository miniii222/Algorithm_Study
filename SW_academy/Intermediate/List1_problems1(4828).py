# -*- coding: utf-8 -*-

'''
4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
'''


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    numbers = list(map(int, input().split()))
    
    
    answer = max(numbers) - min(numbers)
    
    
    print('#{} {}'.format(test_case, answer))