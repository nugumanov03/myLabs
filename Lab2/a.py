
s = input().split()
i=0
while i != s.__len__() :
    print(s[i])
    if s[i] == '0':
        if s[i-1] == '1':
            print('GG')
    i+=1



print(s)