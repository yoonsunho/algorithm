# 0406(일)
# 부분 수열의 합(실버2)
import sys
input = sys.stdin.readline

def dfs(st, total):

    global ans

    if total == S:
        # print(path)
        ans += 1

    for i in range(st, N):
        path.append(arr[i])
        dfs(i+1, total+arr[i])
        path.pop()

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
path = []
dfs(0, 0)
if S == 0:
    ans -= 1
print(ans)