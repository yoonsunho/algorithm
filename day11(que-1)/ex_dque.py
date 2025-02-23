from collections import deque

q = deque()
q.append(1)     # enqueue()
t = q.popleft() # dequeue()

# deque 사용 x(오래걸림)
# list_q = []
# for i in range(100000):
#     list_q.append(i)
# for _ in range(100000):
#     list_q.pop(0)
# print('end')

# deque 사용(시간 단축)
deque_q = deque()
for i in range(1000000):
    deque_q.append(i)
for _ in range(1000000):
    deque_q.popleft()
print('end')