#https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3
#H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
#어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
#어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h가 이 과학자의 H-Index입니다.

#어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

####일단, 발표한 논문 개수보다 인용 수가 많은 논문은 의미x

#%% 뻘짓...
citations = [999,150,765,756,21,23,45,9,1]

def h_index(citations) :
    
    n = len(citations)
    
    #각 논문의 인용수가 모두 발표한 논문보다 많은 경우 ex) [7,4,5]
    if n == len([i for i in citations if i > n]) :
        answer = n
        return answer 
    # [999,150,765,756,21,23,45,9,1] ->8
    else : #[3, 0, 6, 1, 5]	
        answer = max([ j for j in citations if len( [i for i in citations if i >=j ] ) >= j ])
        return answer


h_index(citations)


#%% 최종코드
citations = [999,150,765,756,21,23,45,9,1]
#citations = [7,4,5]
#citations = [3, 0, 6, 1, 5]	
def h_index(citations) :
    n = len(citations)
    citations.sort()
        
    for i in range(n) :
        if citations[i]>=(n-i) :
            return(n-i)
    

h_index(citations)