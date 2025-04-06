# 0325

def find_max():
    result = ''
    n_list = num_list[:]  # 문자열 수정할 거기 때문에 복사해주기

    i = 0
    while i <= K - 1:
        if op[i] == "<":
            cnt = 1
            while (i + cnt) <= (K - 1) and op[i + cnt] == "<":
                cnt += 1
            result += str(n_list.pop(-cnt-1))

        else:  # ">"
            result += str(n_list.pop(-1))
        i += 1
    # print(i)


    result += str(n_list.pop(-1))

    return result

def find_min():
    result = ''
    n_list = num_list[:]  # 문자열 수정할 거기 때문에 복사해주기

    i = 0
    while i <= K-1:
        if op[i] == ">":
            cnt = 1
            while (i+cnt) <= (K-1) and op[i+cnt] == ">":
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