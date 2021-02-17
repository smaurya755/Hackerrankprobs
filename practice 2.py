from collections import defaultdict
d = defaultdict(list)
N = int(input("enter number of values1"))
M = int(input("enter number of values2"))

list1 = []
list2 = []
for i in range(N):
    entry1 = input()
    list1.append(entry1)
for i in range(M):
    entry2 = input()
    list2.append(entry2)
for i in range(N):
    d[list1[i]].append(i+1)
print(d)
for i in range(M):
    if list2[i] in d:
        print(list2[i])
    else:
        print(-1)
