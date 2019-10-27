## count
#### 2d-list에 있는 원소의 개수를 셀 때
```
[mm.count(0) for mm in mylist]
```
- 그냥 for문 두 번 써서 찾는 것보다 빠르다(list comprehension)

## 좌표
#### 2d-list에 있는 원소의 좌표를 구할 때
```
aa = [[x, y] for x, li in enumerate(mylist) for y, val in enumerate(li) if val==2]
bb = [[x, y] for x, li in enumerate(mylist) for y, val in enumerate(li) if val==1]
```
- for문 두 개를 한 번 씩 돌면서, 조건을 만족하는 경우 append하는 것보다 여러 개의 list comprehension을 사용하는 게 더 빠르다.

## COPY
#### 2d-list에서 copy 할 때
```
new = old.copy()
```
new와 old 리스트 각각의 id 값은 달라지지만,
```
id(new[0][0])
id(old[0][0])
```
위의 코드처럼 element를 비교하게 되면, id는 값은 값이 출력

##### 1) copy 패키지
```
from copy import deepcopy
new = deepcopy(old)
```
##### 2) slice
```
new = [mm[:] for mm in old]
```
