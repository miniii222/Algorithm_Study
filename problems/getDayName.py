
#https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3

#2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
#두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
#요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT
#2016년은 윤년입니다.
#%%
a=5; b=24; result = ['TUE']
#%%
def getDayName(a,b) :
    days_month = [31,29,31,30,31,30,31,31,30,31,30,31] #월별 일 수
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    remainder = (sum(days_month[:(a-1)])+b)%7-1
    return(days[remainder])
