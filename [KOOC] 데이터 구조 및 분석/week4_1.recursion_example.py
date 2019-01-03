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
def GCD(numbers) :
    
    A,B = numbers
    
    if B==0 :
        return A
    
    A,B = B, A%B
    numbers = A,B
    return GCD(numbers)

numbers = (105,74)
print(GCD(numbers))
#%%factorial
def Factorial(n) :
    if n==1 or n==0 :
        return 1
    
    return Factorial(n-1) * n

Factorial(5)