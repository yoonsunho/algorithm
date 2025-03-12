# baby-gin 검사
# -> 숫자 3개 연속되었는가?(run)
# -> 숫자 3개가 같은가?(triplet)
# 6자리 숫자 입력
# -> 모든 순서를 보아야 한다(순열)

'''
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''
path = []
visited = [0] * 6
result = False

def is_baby_gin():
    cnt = 0
    # run + triplet 개수의 합 = 2
    # 앞쪽 숫자 세개
    a, b, c = path[0], path[1], path[2]
    if a == b == c:     # triplet
        cnt += 1
    elif a == (b-1) == (c-2):   # run
        cnt += 1

    # 뒤쪽 숫자 세개
    a, b, c = path[3], path[4], path[5]
    if a == b == c:  # triplet
        cnt += 1
    elif a == (b - 1) == (c - 2):  # run
        cnt += 1

    return cnt == 2     # cnt가 2일 때만 True를 반환

def recur(cnt):
    global result
    if cnt == 6:
        # baby-gin 검사
        if is_baby_gin():       # True 반환 받으면
            result = True
        # print(path)
        return

    for idx in range(6):
        # 인덱스를 이미 썼다면 뽑지 마라
        if visited[idx]:
            continue

        visited[idx] = 1
        path.append(arr[idx])
        recur(cnt + 1)
        path.pop()
        visited[idx] = 0


arr = list(map(int, input().split()))

recur(0)

print('YES') if result else print("NO")