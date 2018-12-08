#https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

#�迭 array�� i��° ���ں��� j��° ���ڱ��� �ڸ��� �������� ��, k��°�� �ִ� ���� ���Ϸ� �մϴ�.

#���� ��� array�� [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3�̶��

#array�� 2��°���� 5��°���� �ڸ��� [5, 2, 6, 3]�Դϴ�.
#1���� ���� �迭�� �����ϸ� [2, 3, 5, 6]�Դϴ�.
#2���� ���� �迭�� 3��° ���ڴ� 5�Դϴ�.
#�迭 array, [i, j, k]�� ���ҷ� ���� 2���� �迭 commands�� �Ű������� �־��� ��,
#commands�� ��� ���ҿ� ���� �ռ� ������ ������ �������� �� ���� ����� �迭�� ��� return �ϵ��� solution �Լ��� �ۼ����ּ���.

array = [1,5,2,6,3,7,4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    
    n = len(commands)
    answer = []
    
    for i in range(n) :
        new = array[(commands[i][0]-1) : (commands[i][1])]
        new.sort()
        answer.append(new[(commands[i][2])-1])
        
    return answer

solution(array, commands)