from collections import deque

a  = deque()

a.extend([1,2,3,4,5,6])

print(a)

for i in range(len(a)):
    a.rotate(1)
    print(a)