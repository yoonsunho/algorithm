def recur(i, N, V):
    if i == N:
        return 0
    elif A[i] == V:
        return 1
    else:
        return recur(i+1, N, V)

N = 3
A = [3, 7, 6]
V = 6
ans = recur(0, N, V)
print(ans)
