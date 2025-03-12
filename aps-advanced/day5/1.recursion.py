def BBQ(x):
    x += 10
    print(x)

def KFC(x):
    print(x)
    x += 3
    BBQ(x+2)
    print(x)

x = 3
KFC(x+1)
print(x)

# 4 19 7 3

def mohan(n):
    # 언제 호출 종료시킬까?
    # 항상 종료 조건과 함꼐한다
    if n == 5:
        return

    # 재귀 호출 전 들어가야 할 로직
    print(n,end=" ")
    
    mohan(n+1)  # 다음 재귀 호출(매개 변수를 변경하면서 전달)

    # 돌아오면서 해야 할 로직
    # n = 4 이었을떄 5가 되면서 리턴되고 다시 n = 4 였을 때로 돌아옴
    print(n, end=' ')

mohan(0)
print("End!")

# 0 1 2 3 4 4 3 2 1 0 End!