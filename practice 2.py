from collections import defaultdict
d = defaultdict(list)
N,  M = map(int, input().split())
list1 = []
for i in range(N):
    d[input()].append(i+1)
for i in range(M):
    list1.append(input())
for i in list1:
    if i in d:
        print(" ".join(map(str, d[i])))
    else:
        print(-1)

