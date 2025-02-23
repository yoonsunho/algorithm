# 큐 생성
queue = [0] * 3
front = rear = -1

# 1,2,3 인큐
rear += 1       # enqueue 1
queue[rear] = 1

rear += 1       # enqueue 1
queue[rear] = 2

rear += 1       # enqueue 1
queue[rear] = 3

while front != rear:    # 큐에 원소가 남아있으면
    front += 1      # dequeue
    t = queue[front]
    print(t)
print(queue)

'''
front += 1      # dequeue
print(queue[front])     # 1

front += 1      # dequeue
print(queue[front])     # 2

front += 1      # dequeue
print(queue[front])     # 3
'''

q = []
q.append(1)     # enqueue 1
print(q)        # [1]
q.append(2)
print(q)        # [1,2]
q.append(3)
print(q)        # [1,2,3]
print(q.pop(0))     # dequeue # 1
print(q)        # [2,3]
print(q.pop(0)) # 2
print(q)        # [3]
print(q.pop(0)) # 3
print(q)        # []