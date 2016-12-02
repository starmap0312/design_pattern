import collections

q = collections.deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q.popleft())
print(q.popleft())
q.append(4)
print(q)
q.appendleft(5)
print(q)
