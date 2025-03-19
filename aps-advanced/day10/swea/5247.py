import sys
sys.stdin = open("txt/5247.txt", "r")

# deque 사용

from collections import deque

def bfs():

    dp = [-1] * 10000001    # dp[i] : 숫자 i 를 만들기 위해 필요한 최소 연산의 수
    q = deque([N])
    dp[N] = 0

    while q:

        num = q.popleft()

        if num == M:
            return dp[num]

        for next_num in [num+1, num-1,num*2,num-10]:
            if 1 <= next_num <= 1000000 and dp[next_num] == -1:
                dp[next_num] =dp[num] + 1
                q.append(next_num)
    

T = int(input())
for tc in range(1, T+1):

    N, M = map(int,input().split())     # 자연수
    answer = bfs()

    print(f'#{tc} {answer}')