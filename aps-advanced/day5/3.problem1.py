# 주사위 3 개를 던져 합이 10 이하인 경우는 몇개?
# 종료 조건: 3번 던진다
# 나올 수 있는 범위 : 주사위는 1~6

path = []
result = 0

def recur(cnt,total):
    global result

    # 만약 total 이 이미 10을 넘었으면 볼 필요도 없음
    # 기저 조건에서 경우의 수를 많이 줄여줌
    if total > 10:
        return

    if cnt == 3:
        # 합리 10 이하인건 몇개?
        # sum: path길이만큼 반복되기 때문에 비효율(O(n))
        # if sum(path) <= 10:
        #     result += 1
        #     print(path)
        # return
        if total <= 10:
            result += 1
            print(path)
        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1, total + num)
        path.pop()

recur(0, 0)
print(result)