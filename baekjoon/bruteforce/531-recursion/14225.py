# 0407(월)
# 부분수열의 합(실버1)
import sys
input = sys.stdin.readline

def recur(cnt, total):
    global ans_list

    if cnt == N:
        ans_list.append(total)
        return

    recur(cnt+1, total+arr[cnt])
    recur(cnt+1, total)


N = int(input())

arr = list(map(int, input().split()))
ans_list = []


recur(0,0)
ans_list.sort()
ar = set(ans_list)      # 시간단축기위해 인덱스 변호로 조회하려고 set 처리

new_arr = list(map(int, ar))    # 인덱스 조회 하기위해 다시 리스트 처리

i = 0
ans = ans_list[-1]+1
while(i < new_arr[-1]):
    if i != new_arr[i]:
        ans = i
        break
    i += 1

print(ans)