
import queue

queue = queue.deque()

N = int(input())

for _ in range(N):
    flag, *value = input().split()
    if flag == "i":
        queue.appendleft(int(value[0]))
    elif flag == "o":
        if queue:
            print(queue.pop())
        else:
            print("empty")
    elif flag == "c":
        print(len(queue))