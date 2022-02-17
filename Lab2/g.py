n = int(input())


cntli = {}
for i in range(n):
    mi = input().split()
    name = mi[0]
    sila = mi[1]

    k = 1
    try:
        k = k + int(cntli[sila])
    except :
        k = k 

    cntli[sila] = k

d = int(input())


cntli2 = {}
for i in range(d):
    mi2=  input().split()
    nameD = mi2[0]
    silaD = mi2[1]
    chisl = int(mi2[2])
    k = chisl
    try:
        k = k + int(cntli2[silaD])
    except :
        k = k 
    cntli2[silaD] = k
   

demonans = 0
for i in cntli.keys():
    if i in cntli2.keys():
        if cntli[i] - cntli2[i] >= 0:
            demonans += cntli[i] - cntli2[i]
    else:
        demonans += cntli[i]


print('Demons left:', demonans)
