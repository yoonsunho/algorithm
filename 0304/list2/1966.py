import sys
sys.stdin = open("txt/1966.txt","r")

# 버블정렬로 한번쯤 다시 해보기

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = list(map(int,input().split()))
    new_arr = sorted(arr)
    print(f'#{tc} {" ".join(map(str,new_arr))}')