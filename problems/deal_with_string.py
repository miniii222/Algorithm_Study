# -*- coding: utf-8 -*-
#https://programmers.co.kr/learn/courses/30/lessons/12926
#문자열 s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수, solution을 완성하세요.
#예를들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

s = "a234" #False
s = "4357" #True

#%%
#내 풀이

def deal_with_string(s):
    try :
        int(s)
        
        l = len(s)
        if l==4 or l==6 :
            return True
        else :
            return False

    except :
        return False
    
#%%
#참고한 풀이
def deal_with_string2(s) :
    return s.isdigit() and len(s) in [4,6]