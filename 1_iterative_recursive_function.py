import time

########C language to python language


#Data Structure
## 1) factorial 함수
###반복적 정의

"""
int fact (int n) {
        if (n==0) return (1);
        else return (n*fact(n-1));
}
"""

def factorial_iter(n) :
    fact = 1
    for i in range(1,n+1) :
        fact = fact * i
        
    return(fact)
    
start = time.time()
factorial_iter(50)
end = time.time()

print("factorial_iter : " , end-start)


###재귀적 정의
"""
int fib (int n) {
        if (n==0) return (0);
        else if (n==1) return (1);
        else return (fib(n-1) + fib(n-2));
}
"""

def factorial_recur(n) :
    if n==0 :
        return 1
    else :
        return(n*factorial_recur(n-1))

start = time.time()
factorial_recur(50)
end = time.time()

print("factorial_recur : " , end-start)     


##2) fibonacci 수열
### 반복적 정의
"""
int fib(int n) {
        int fn, fn1, fn2, i;
        fn2 = 0; fn1 = 1;
        for (i=2; i<=n; i++) {
                        fn = fn1 + fn2;
                        fn2 = fn1;
                        fn1 = fn;

        return(fn);
}
"""

def fibo_iter(n) :
    fib0=0; fib1=1;
    
    if n==0 :
        return (fib0)
    elif n==1 :
        return (fib1)
    
    else :
        for i in range(n-1) :
            fib = fib1+fib0
            fib0=fib1
            fib1=fib
            
        return(fib)
           
fibo_iter(5)





### 재귀적 정의
"""
int fib (int n) {
        if (n==0) return (0);
        else if (n==1) return (1);
        else return (fib(n-1) + fib(n-2));
}
"""
def fibo_recur(n) :
    if n==0 :
        return 0
    elif n==1 :
        return 1
    else :
        return(fibo_recur(n-1) + fibo_recur(n-2))

fibo_recur(5)

##3) 하노이 탑
### 재귀적 정의
"""
void towerHanoi (char from, char to, char aux, int n) {
        /* aux를 이용하여 from 으로부터 to로 n개의 디스크를 옮김 */
        if (n==1)
        printf("Move disc 1 from peg %c to peg %c\n", from, to);
        else {
                towerHanoi(from, aux, to, n-1);
                printf("Move disc %d from peg %c to peg %c\n", n, from, to);
                towerHanoi(aux, to, from, n-1);
                }
}
"""

def towerHanoi(start, end, aux, n) :
    
    if n==1 :
        print("Move disc 1 from peg",start,"to peg", end)
    else :
        towerHanoi(start, end, aux, n-1)
        print("Move disc",n,"from peg",start,"to peg",end)
        towerHanoi(aux,end,start, n-1)
        
towerHanoi("A","C","B",5)
