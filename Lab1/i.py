subS = '@gmail.com'

ManySt = []
OutpuSt = []
len = int(input())

i = 0
while i != len:
    ManySt.append(input())
    i+=1


i= 0
while i != len:
    sub = ManySt[i].find(subS)
    mnstr = ''
    if sub > -1:
            string = ManySt[i]
            k = 0
            for char in string:
                    if k < sub:
                        mnstr += char    
                    k+=1

    i+=1
    OutpuSt.append(mnstr)


for something in OutpuSt:
    if something != '':
        print(something)



