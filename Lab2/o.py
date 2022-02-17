
def converter(string , k):
    li = [
        ('ONE', 1 ),
        ('TWO', 2 ),
        ('THR', 3 ),
        ('FOU', 4 ),
        ('FIV', 5 ),
        ('SIX', 6 ),     
        ('SEV', 7 ),
        ('EIG', 8 ),
        ('NIN', 9 ),
        ('ZER', 0 )
    ]
    if k == 1:
        for i in li:
            if string == i[0]:
                return i[1]        
    else:
        for i in li:
            if string == str(i[1]):
                return i[0]   

s =input().split(sep='+')
sum = 0
for m in s:
    stroka = 0
    k = [m[i:i + 3] for i in range(0, len(m), 3)]
    for i in k:
        stroka= 10*stroka + converter(i,1)
    sum +=stroka

for i in str(sum):
    print(converter(i,2),end='')
    