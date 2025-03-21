# 수열 정렬

N = int(input())    # 배열 a의 길이(1<= N<= 50)

A = list(map(int,input().split()))
sort_A = sorted(A)
# print(sort_A)
cnt = -1
arr = [0]*N
for x in sort_A:
    for i in range(N):
        if A[i] == x:
            A[i] = -1
            cnt += 1
            arr[i] = cnt
            break

# print(arr)
print(" ".join(map(str, arr)))