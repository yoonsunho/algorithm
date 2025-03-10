import sys
sys.stdin = open("txt/3499.txt", "r")
from collections import deque

def perfect_shuffle(arr):



T = int(input())

for tc in range(1,T+1):

    N = int(input())

    arr = deque(list(input().split()))
    perfect_shuffle(arr)

    print(f'#{tc}')