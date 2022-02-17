leng = int(input())

li = {}
for i in range(leng):
    mi = input().split()
    i = str(mi[0])
    k = int(mi[1])
    try:
        k = k + int(li[i])
    except :
        k = k 
    li[i]=k


max = 0

for i in li.values():
    if max < i:
        max = i



otvet = []
for i in li.keys():
    if li[i] != max:
        otvet.append(f'{i} has to receive {max -li[i]} tenge')
    else:
        otvet.append(f'{i} is lucky!')
otvet.sort()
for i in otvet:
    print(i)