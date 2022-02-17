


n = int(input())
li = []
li1 = []
for i in range(n):
    stroka = input().split()
    task = stroka[0]
    if task == '1':
        book = stroka[1]
        li.append(book)
    else:
        li1.append(li[0])
        del li[0]
for i in li1:
    print(i,end=' ')
