# 카드 5 장을 뽑아서
# 5장 뽑았을 때, 연손된 3 개가 나오면 counting

card = ['A', 'J', 'Q', 'K']
path = []
result = 0

def count_three():
    for i in range(3):
        if path[i] == path[i+1] == path[i+2]:
            return True

def recur(cnt):
    global result

    if cnt == 5:
        # 연속된3 개가 나오면 couting
        if count_three():
            result += 1
            print(path)
        return

    for idx in range(4):
        path.append(card[idx])
        recur(cnt + 1)
        path.pop()


recur(0)
print(result)