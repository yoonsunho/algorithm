import sys
sys.stdin = open("txt/5203.txt", "r")

def is_babygin(arr):

    n = len(arr)
    visited = [0] * 12
    for a in arr:
        visited[a] += 1

    for i in range(n+2):
        if visited[i] >= 3:
            visited[i] -= 3
            return 1
        elif visited[i] >= 1 and visited[i+1] >= 1 and visited[i+2] >= 1:
            return 1
    return 0

    # print(arr)
    # for i in range(n-2):
    #     if arr[i] == arr[i+1] == arr[i+2]:
    #         return 1
    #     if arr[i] == arr[i+1] - 1 == arr[i+2] - 2:
    #         return 1
    #     if arr[i] == arr[i+1] + 1 == arr[i+2] + 2:
    #         return 1
    # return 0


def play(p1,p2):
    n = len(p1)
    for i in range(3, n+1):
        a1 = p1[:i]
        a2 = p2[:i]
        if is_babygin(a1) == 1:
            # print(a1)
            return 1
        if is_babygin(a2) == 1:
            # print(a2)
            return 2

    else:
        return 0

T = int(input())
for tc in range(1, T+1):

    num_card = list(map(int, input().split()))
    # num_card.sort()
    # print(num_card)
    player1, player2 = [], []
    for i in range(6):
        player1.append(num_card[i*2])
        player2.append(num_card[i*2+1])

    # print(player1)
    # print(player2)

    ans = play(player1, player2)

    print(f'#{tc} {ans}')