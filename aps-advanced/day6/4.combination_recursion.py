arr = ['A','B','C','D','E']
n= 3

path = []
# 5명 중 3명을 뽑는 문제
def recur(cnt, start):
    if cnt == n:
        print(*path)
        return 
    
    # 5명을 고려해야한다
    # start: 이전 재귀로 부터 넘겨 받아야하는 값
    for i in range(start, len(arr)):      # range(이전에 뽑았던 인덱스 +1 부터,N)
        path.append(arr[i])
        # i : i 번째를 뽑겠다
        # i + 1을 매개변수로 전달 : 다음 재귀부터는 i+1부터 고려
        recur(cnt + 1, i+1)
        path.pop()



recur(0,0)