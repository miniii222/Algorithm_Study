# -*- coding: utf-8 -*-

#%%fibonacci
def Fibonacci(n) :
    if n==0 :
        return 0
    if n==1 :
        return 1
    return Fibonacci(n-1)+Fibonacci(n-2) # n의 size가 줄어든다.

for itr in range(10) :
    print(Fibonacci(itr))
    
#%%GCD A와 B의 최대공약수를 Euclid's algorithm을 이용하여 구한다.
def GCD(A,B) :
        
    if B==0 :
        return A
    
    A,B = B, A%B
    return(A, B)

#%%factorial


a = 32; b = 24
a,b = b, a%b

print(GCD(32,24))
