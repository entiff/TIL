# Kruskal Algorithm
"""
비용이 낮은 것 부터 잇는다
순환이 생기지 않게 한다
모든 노드를 하나씩 거친다
"""

# 체육복 문제
"""
전체 학생의 수 n
체육복을 도난당한 학생들의 번호 배열 lost
여벌의 체육복을 가져온 학생들의 번호 배열 reserve
체육 수업 들을 수 있는 학생들의 최댓값을 return
"""


def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    lost_1 = lost.copy()
    reserve_1 = reserve.copy()
    for student in lost_1:
        if student in reserve_1:
            lost.remove(student)
            reserve.remove(student)
            answer += 1

    for student in lost:
        # 앞 친구가 갖고 있어?
        if student - 1 in reserve:
            answer += 1
            reserve.remove(student - 1)

        # 뒤 친구가 갖고 있어?
        elif student + 1 in reserve:
            answer += 1
            reserve.remove(student + 1)
    return answer
