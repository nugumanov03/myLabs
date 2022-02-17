

s = input()
k= 0
li = []
for i in s:
    li.append(i)

for i in li:
    try:   
        if i == '{':
            li.pop(li.index('}'))
            li.pop(li.index(i))  
        if i == '[':
            li.pop(li.index(']'))
            li.pop(li.index(i))   
        if i == '(':
            li.pop(li.index(')'))
            li.pop(li.index(i))  
    except:
        k +=2
if li.__len__() == 0:
    print('Yes')
else:
    print('No')
    
