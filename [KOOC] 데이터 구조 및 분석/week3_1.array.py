#########1. Insert procedure in array##########

x = ['a', 'b', 'd','e','f']

idxInsert = 2; valInsert = 'c' #2번째에 'c'라는 값을 넣을 것

y = [None] * 6
for i in range(idxInsert) : #넣으려고 하는 자리 전까지는 x값을 그대로
    y[i] = x[i]
    
y[idxInsert] = valInsert #추가

for i in range(idxInsert, len(x)) : #그 다음 값들 x랑 동일하게
    y[i+1] = x[i]
    

x=y #y의 reference를 x에 저장

#n번의 data operation 필요

#########2. delete procedure in array##########
idxDelete = 3
y = [None] * 5

for i in range(idxDelete) : #지우려는 값 전까지는 그대로
    y[i] = x[i]
    
for i in range(idxDelete+1, len(x)) : #지운 거 빼고 그대로
    y[i-1] = x[i]
    
x=y

#n-1번의 operation 수행
