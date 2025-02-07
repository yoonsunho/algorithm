# 5x5 2차원 배열에 25개의 숫자를 저장하고 대각선 원소의 합 구하기
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
s = 0
for i in range(5):
    s += A[i][i]
    s += A[i][4-i]
s -= A[5//2][5//2]
print(s)

# 연습문제 2
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N):
    for j in range(5):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                total += abs(arr[ni, nj]-arr[i][j])
print(total)