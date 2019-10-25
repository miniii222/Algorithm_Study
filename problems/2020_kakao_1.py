# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:15:55 2019

"""
#https://programmers.co.kr/learn/courses/30/lessons/60057
s = "aabbaccc"
s = "abcabcabcabcdededededede"
n = len(s)

#%%

def solution(s) :
    n = len(s)

    if n == 1 :
        return 1

    length_list = []
    ss = s
    nn = len(ss)//2

    for s_len in range(1, nn+1) :
        s = ss

        n = len(s)
        j = 0

        while j < n :
            cnt =1
            for i in range(j + s_len, n, s_len) :

                if s[j : j + s_len] == s[i : i + s_len] :

                    cnt += 1
                else :
                    break

            if cnt > 1:
                s = s[:j] + str(cnt)+ s[j:j + s_len] + s[j + s_len * cnt:]
                n = len(s)
                j += s_len * cnt - (cnt - 1) * s_len + len(str(cnt))
            else :
                j += s_len

        length_list.append(len(s))

    answer = min(length_list)

    return answer