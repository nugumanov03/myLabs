
s = input().split()
s.sort()
li = []

for i in s:
    slovo = ''
    for k in i:
        if k.isalpha():
            slovo+=k
    li.append(slovo)
li1 = []
for i in li:
    if i not in li1:
        li1.append(i)
li1.sort()
print(li1.__len__())
for i in li1:
    print(i)