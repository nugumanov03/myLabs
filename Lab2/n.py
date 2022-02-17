li = []
while True:
    string = input()
    if string == '0':
        break
    li.append(int(string))

len = li.__len__()
li2 = []

i = 0
while i != len:
    sum = 0
    if i != len-1-i:
        sum+= li[i]+li[len-i-1] 
    else:
        sum = li[i]
    if i < len - i:    
        li2.append(sum)
    i+=1
for i in li2:
    print(i , end=' ')