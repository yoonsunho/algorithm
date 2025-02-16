import sys
sys.stdin = open("txt/1954.txt", "r")
# 다시 풀어보기..

def snail(i,j,arr,dir):
    ni = i + di[dir]
    nj = j + dj[dir]
    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]==0:
        arr[ni][nj] = arr[i][j]+1
        return snail(ni,nj,arr,dir)
    else:
        # 방향 전환
        next_dir = (dir+1) % 4
        ni = i + di[next_dir]
        nj = j + dj[next_dir]
        if 0 <= ni < N and 0 <= nj <N and arr[ni][nj] == 0:
            arr[ni][nj] = arr[i][j]+1
            return snail(ni, nj, arr, next_dir)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    N = int(input())
    # 새로운 배열 만들어주기
    matrix = [[0]*N for _ in range(N)]
    matrix[0][0] = 1

    snail(0,0,matrix,0)

    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")
        print()