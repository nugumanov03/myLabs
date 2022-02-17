leng = int(input())
i = 0
while i != leng:
    k=0
    while k != leng:
        if i == k:
            print(i*k,end= ' ')
        elif i == 0:
            print(k,end=' ')
        elif k == 0:
            print(i , end= ' ')
        else:
            print(0,end= ' ')
        k+=1
    print(' ')
    i+=1