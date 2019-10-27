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
