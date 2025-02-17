'''
3
5 1
1 1 0 0 1
1 3 2
5 3
1 1 0 0 1
1 3 2
1 4 1
1 2 4
5 1
1 1 0 1 0
1 4 1

#1 1 1 1 1 1
#2 1 0 0 1 0
#3 1 1 0 0 0
'''

T = int(input())

for tc in range(1, T+1):

     N, M = map(int, input().split())   # N : 팀원 수 # M : 명령 수( 3<=N<=20, 1<=M<=10,)

     arr = list(map(int, input().split())) # n명의 초기 상태

     for _ in range(M):

         command = list(map(int, input().split()))  #  (a==1, 1<=b, c<=N)

         if command[1] + command[2] - 1 <= N:
             for i in range(command[1]-1, command[1] + command[2] - 1):
                 arr[i] = 1 - arr[i]
         else:
             for i in range(command[1]-1, N):
                 arr[i] = 1 - arr[i]


     print(f'#{tc} {" ".join(map(str,arr))}')
