from operator import itemgetter, attrgetter, methodcaller
li = []
while True:
    string = input()
    if string == '0':
        break
    
    li.append(string.split())
li1 = []
for i in li:
    k = i[0]
    k2 = i[1]
    k3 = i[2]
    li1.append((k3,k2, k))
li1.sort()
for i in li1:
    print(i[2],i[1],i[0])
