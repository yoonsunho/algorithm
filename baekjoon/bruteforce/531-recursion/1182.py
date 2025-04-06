# 0406(일)
# 부분 수열의 합(실버2)

# 처음에 recur문을 for문 안에넣는 어이없는 짓을 함...

import sys
input = sys.stdin.readline

def recur(cnt,total,usage):

    global ans

    if cnt == N:
        if usage != 0 and total == S:
            ans += 1
        return

    recur(cnt+1, total, usage)
    recur(cnt+1, total+arr[cnt], usage+1)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

recur(0, 0, 0)
print(ans)