#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

#수많은 마라톤 선수들이 마라톤에 참여하였습니다.
#단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
#마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
#완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
#%%
participant = ['leo', 'kiki', 'eden']; completion= ['eden', 'kiki']
participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']	; completion = ['josipa', 'filipa', 'marina', 'nikola']
participant = ['mislav', 'stanko', 'mislav', 'ana'];	completion = ['stanko', 'ana', 'mislav']

#%%
def not_complete(participant, completion) :
    participant.sort(); completion.sort()
    n = len(participant)
    answer = [participant[i] for i in range(n-1) if participant[i] != completion[i]]
    
    if len(answer)==0 :
        return(participant[n-1])
    else :
        return(answer[0])

#%%
participant.sort(); completion.sort()

for p,c in zip(participant,completion):
    print(p, c)
    if p!=c : print(p)
#%% 시간초과 나온 코드...!
not_completed = set((x,participant.count(x)) for x in set(participant))-set((x,completion.count(x)) for x in set(completion))
answer = not_completed.pop()[0]
