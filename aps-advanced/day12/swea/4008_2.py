import sys
sys.stdin = open("txt/4008.txt", "r")
op = ['+','-','*','/']

def do_count(arr):

    # total = 0
    total = num_list[0]

    for i in range(len(arr)):

        num = num_list[i+1]
        # n2 = num_list[i+1]
        if arr[i] == '+':
            total += num
            # print(total)
        elif arr[i] == '-':
            total -= num
        elif arr[i] == "*":
            total *= num
        else:
            total = int(total/num)

    # print(total)
    return total

def permu_oper(cnt):

    global path
    global min_v, max_v

    if cnt == N - 1:
        # print(path)
        min_v = min(min_v, do_count(path))
        max_v = max(max_v, do_count(path))
        return

    for i in range(N-1):
            
        # 방문을 했거나, 중복 요소 제거
        if visited[i] or (i > 0 and op_list[i] == op_list[i-1] and visited[i-1] == 0):
            continue

        visited[i] = 1
        path.append(op_list[i])
        permu_oper(cnt+1)
        path.pop()
        visited[i] = 0
        # path.pop()


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    # print(N)
    op_num = list(map(int, input().split()))
    # print(op_num)
    op_list = []        # 연산자들을 담을 리스트
    for i in range(4):
        op_list.extend(op[i]*op_num[i])
    # print(op_list)
    num_list = list(map(int, input().split()))
    # print(num_list)

    visited = [0]*(N-1)
    path = []
    min_v = float('inf')
    max_v = -float('inf')
    permu_oper(0)


    print(f'#{tc} {max_v-min_v}')