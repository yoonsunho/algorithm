# 0325

def find_max():
    # result = ''
    n_list = num_list[:]    # 문자열 수정할 거기 때문에 복사해주기

    if op[0] == ">":    # 초기값 지정해주기
        result = '9'
        n_list.pop()
    else:
        cnt = 0
        while op[cnt] == "<":
            cnt += 1
        result = str(n_list.pop(K-cnt-1))
        n_list.pop(K-cnt-1)

    i = 0
    while i <= K-2:
        if op[i] == ">":
            cnt = 0
            while (i + cnt + 1) <= K-1 and op[i+cnt+1] == "<":
                cnt += 1
            # print(cnt)
            result += str(n_list.pop(len(n_list)-1-cnt))
        else:   # "<" 만났을 때
            cnt = 0
            while (i + cnt + 1) <= K-1 and op[i+cnt+1] == "<":
                cnt += 1
            # print(cnt)
            result += str(n_list.pop(len(n_list)-1-cnt))
            # print(result)
        i += 1

    result += str(n_list.pop())

    # print(result)
    return result

def find_min():
    result = ''
    n_list = num_list[:]  # 문자열 수정할 거기 때문에 복사해주기

    i = 0
    while i <= K-1:
        if op[i] == ">":
            cnt = 1
            while (i+cnt)<= K-1 and op[i+cnt] == ">":
                cnt += 1
            result += str(n_list.pop(cnt))

        else:   # "<"
            result += str(n_list.pop(0))
        i += 1

    result += str(n_list.pop(0))

    return result

K = int(input())    # 부등호의 개수 (2 <= K <= 9)
op = list(input().split())


num_list = [i for i in range(10)]   # 0 ~ 9 사이의 수를 담아놓을 리스트
# print(num_list)
# print(op)

# min_v = float('inf')
# max_v = -float('inf')

min_v = find_min()
max_v = find_max()
# print(num_list.pop())
print(max_v)
print(min_v)