# 내 풀이
arr = list(input())

N = len(arr)    # 1<=N<=1000

for i in range(N):
    if arr[i] == 'Y':
        arr[i] = 1
    else:
        arr[i] = 0
count = 0

for i in range(1, N+1):
    if arr[i-1] == 1:
        count += 1
        arr[i-1] -= 1
        for j in range(i+1, N+1):
            if j % i == 0:
                arr[j-1] = 1 - arr[j-1]
print(count)

# 강사님 풀이
arr = list(input())

N = len(arr)    # 1<=N<=1000

for i in range(N):
    if arr[i] == 'Y':
        arr[i] = 1
    else:
        arr[i] = 0
count = 0

for i in range(1, N+1):
    if arr[i-1] == 1:
        count += 1
        arr[i-1] -= 1
        for j in range(i+1, N+1):
            if j % i == 0:
                arr[j-1] = 1 - arr[j-1]

# 이 부분 추가 # 모든 전구를 끌 수 없다면 -1 출력
for a in arr:
    if a == 0:
        print("-1")
        break
else:
    print(count)

