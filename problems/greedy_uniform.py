# -*- coding: utf-8 -*-

#https://programmers.co.kr/learn/courses/30/lessons/42862
#오늘은 체육수업이 있는 날입니다. 그런데 점심시간에 도둑이 들어 몇몇 학생의 체육복이 도난을 당했습니다.
#다행히 일부 학생들이 여벌의 체육복을 가져왔습니다.
#학생들의 번호는 체격 순으로 매겨져 있기 때문에 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려주려고 합니다.

#예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
#당연히 체육복을 2벌 가져온 학생의 체육복이 도난을 당했다면, 여벌의 체육복을 빌려줄 수 없습니다.

#전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
#여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
#체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

#%%
n=5; lost =[2, 4]; reserve=[1, 3, 5]

#%%
def greedy_unifrom(n, lost, reserve) :
    student = [1]*n
    
    for i in [st-1 for st in reserve] :
        student[i] = student[i]+1
        
    for i in [st-1 for st in lost] :
        student[i] = student[i]-1
        
    for i in range(n-1) :
        if student[i] == 2 and student[i+1] ==0 :
            student[i]=1
            student[i+1]=1
            
    for i in range(n-1,0,-1) :
        if student[i] == 2 and student[i-1] ==0 :
            student[i]=1
            student[i-1]=1
            
    answer = len([ii for ii in student if ii>=1])
    
    return answer
