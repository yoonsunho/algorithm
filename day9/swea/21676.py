# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 프로그래머스
'''
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2
'''
path = []
cnt = 0
result = 0
def solution(numbers, target, cnt):
    global result
    n = len(numbers)
    sum_v = 0

    if cnt == n:
        # print(path)
        for i in range(n):
            sum_v += int(path[i] + str(numbers[i]))
        if sum_v == target:
            result += 1
        return

    # elif cnt > n:
    #     return

    for oper in ['+','-']:
        # print(oper)
        path.append(oper)
        solution(numbers, target, cnt+1)
        path.pop()


    return result


numbers = [4, 1, 2, 1]
target = 4

print(solution(numbers,target,cnt))
# print(answer)