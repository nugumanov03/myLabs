leng = int(input())
i=0
if leng %2== 0:

    while i != leng:
        k= 0
        while k != leng:
            if k <= i:
                print('#',end= '')
            else:
                print('.',end='')
            k+=1
        i+=1
        print(' ')
else:
    while i != leng:
        k= 0
        while k != leng:
            if i < leng-k-1:
                print('.',end= '')
            else:
                print('#',end='')
            k+=1
        i+=1
        print(' ')
