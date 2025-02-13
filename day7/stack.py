s = []
def push(arr,item):
    arr.append(item)
    return arr

print(push(s,3))
print(push(s,4))
print(push(s,'a'))

# push
# 디버깅 방법 (굳이 이 방법 쓰지 않아도 됨ㅁ)
def push_(item,size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack = [0] * size
top = -1

push_(10, size)

# 간단하게 이렇게만 구현해도 됨
# top += 1
# stack[top] = 20
print(stack)

# pop
# 디버기용 방법
# def pop():
#     global top
#     if top == -1:
#         print('underflow!')
#         return 0
#     else:
#         top -= 1
#         return stack[top+1]
#
# print(pop())
# print(stack)

# 간단 방법
if top > -1:
    top -= 1
    print(stack[top+1])
print(stack)
