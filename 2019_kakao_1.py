# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 01:44:21 2019

@author: Seungmini
"""

#https://programmers.co.kr/learn/courses/30/lessons/60058

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
          "Enter uid1234 Prodo","Change uid4567 Ryan"]
record = [rr.split(' ') for rr in record]

["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", 
 "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
#%%
def solution(record):

    record = [rr.split(' ') for rr in record]
    action = [rr[0] for rr in record if rr[0] != 'Change']
    uid = [rr[1] for rr in record if rr[0] != 'Change']
    id_name = {rec[1] : rec[2] for rec in record if len(rec) > 2}

    action_dict = {'Enter' : '들어왔습니다.', 'Leave' : '나갔습니다.'}
    action = [action_dict[aa] for aa in action]

    name = [id_name[uu] for uu in uid]
    result = [m + '님이 ' + n for m,n in zip(name, action)]

    return result