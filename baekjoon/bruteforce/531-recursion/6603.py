# 0406(일)
# 로또(실버2)

def make_combination(cnt, st):
    global roto

    if cnt == 6:
        print(' '.join(map(str, roto)))
        return

    for i in range(st, k):
        if visited[i]:
            continue
        visited[i] = 1
        roto.append(s[i])
        make_combination(cnt +1, i+1)
        visited[i] = 0
        roto.pop()

while True:
    arr = list(map(int, input().split()))
    
    if arr[0] == 0:     # 종료조건 만남
        break

    k = arr[0]
    s = arr[1:]
    roto =[]
    visited = [0]*k
    make_combination(0,0)
    print()
    # print(k, s)

