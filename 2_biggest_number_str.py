
numbers = [3, 30, 34, 547, 9,1000]
n = len(numbers)

#%%뻘짓..
str_list = list(map(str, numbers))
str_len = list(map(len, str_list))
max_len = len(max(str_list, key = len))

for i in range(n) :
    for j in range(max_len-str_len[i]) :    #가장 자릿수가 큰 숫자를 기준으로 
        str_list[i] = str_list[i]+"0"       #모든 숫자들의 길이를 0을 추가하여 맞춰줌


#같은 자릿수의 숫자들을 기준으로 내림차순 정렬       
sort_index = sorted(range(len(str_list)), key=lambda ix: str_list[ix],reverse=True)

#자릿수를 같게 했을 때 다른 숫자인데 같은 숫자로 되는 경우 처리
for i in range(1,n) :
    if str_list[sort_index[i-1]]==str_list[sort_index[i]] and numbers[sort_index[i-1]]>numbers[sort_index[i]]:
        
        #정렬을 했기 때문에 같은 숫자끼리는 이웃할 것.
        #원래 주어진 숫자를 기준으로 자릿수가 낮은 것이 먼저 나와야 함.
        sort_index[i-1], sort_index[i] = sort_index[i], sort_index[i-1]
        
    
answer=""
for i in sort_index :
    answer=answer+str(numbers[i])
    
print(answer)

#이 알고리즘은 numbers = [30,33,3,331] 같은 경우에는 x ㅜㅜ
#%%
"""
[(i,num) for i, num in sorted(enumerate(str_list), key = lambda v : v[1])]
sorted(enumerate(str_list), key = lambda v : v[1])
"""

#%%
#numbers = [30,33,3,331,37]
#numbers = [100,11,101,1,111]
numbers = [0,0,0,7,70]
n = len(numbers)

def biggest_num_string(numbers) :

    if not any(numbers)  :  #모든 원소가 0인 경우
        return "0"
    else :
        str_list = list(map(str,numbers)) #number->string
        max_len = max(list(map(len, str_list))) #string length
        
        sort_key = lambda x : x + x[-1]*(max_len - len(x)) #자릿수를 맞추어 주되, 마지막 숫자를 반복하여 맞춘다.
        return "".join(sorted(str_list, key = sort_key, reverse = True))
    
biggest_num_string(numbers)
#test돌려보면 일부 틀리다고 나옴
#https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3