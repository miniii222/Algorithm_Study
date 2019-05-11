# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:30:02 2019

@author: Seungmini
"""

#https://programmers.co.kr/learn/courses/30/lessons/12981
n = 3
words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 
         'mother', 'robot', 'tank']

n = 2
words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
#%%
word_list = []
nn = len(words)
i = 0

for word in words :
    
    
    if i== 0 : #첫 번째 사람은 그냥 패스
        word_list.append(word)
        i+=1
    elif word in word_list : #앞 사람이 말한 단어를 말한 경우
        break
    
    elif word_list[-1][-1] == word[0] : #앞 사람이 말한 단어를 말하지 않았고, 끝말잇기를 잘 한 경우
        word_list.append(word)
        i+=1
    else :
        break
        
#%%
i+=1
if i > nn : #탈락자가 발생하지 않은 경우
    answer = [0,0]

elif i%n == 0 :
    
    answer = [n, i//n]

else :
    
    answer = [i%n, i//n+1]
    
answer
